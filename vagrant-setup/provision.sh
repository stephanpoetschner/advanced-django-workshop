#!/usr/bin/env bash

export PROJECT_NAME=django_advanced
#export PYTHON_VERSION=python
export PYTHON_VERSION=python3

## general config ##
# Disabling UI for debconf. (See `man debconf` for more options.)
export DEBIAN_FRONTEND=noninteractive

set -e # Exit script immediately on first error.
set -x # Print commands and their arguments as they are executed.

# set time zone
area="Europe"
zone="Vienna"
sudo sh -c "echo \"$area/$zone\" > /tmp/timezone"
sudo cp -f /tmp/timezone /etc/timezone
sudo cp -f /usr/share/zoneinfo/$area/$zone /etc/localtime


export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

locale-gen en_US.UTF-8
sudo dpkg-reconfigure locales

cat << EOF >> $HOME/.bashrc

export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

export VIRTUALENVWRAPPER_PYTHON=/usr/bin/${PYTHON_VERSION}

EOF

# update package manager resources
sudo apt-get update -y

sudo update-alternatives --set editor /usr/bin/vim.basic

## end general config ##

## database

sudo apt-get install -y postgresql postgresql-contrib
sudo apt-get build-dep -y ${PYTHON_VERSION}-psycopg2


APP_DB_USER=${PROJECT_NAME}
APP_DB_PASS=${PROJECT_NAME}

APP_DB_NAME=${PROJECT_NAME}

cat << EOF | sudo -u postgres psql
-- Create the database user:
CREATE USER $APP_DB_USER WITH CREATEDB PASSWORD '$APP_DB_PASS';

-- Create the database:
CREATE DATABASE $APP_DB_NAME WITH OWNER=$APP_DB_USER
                                  LC_COLLATE='en_US.utf8'
                                  LC_CTYPE='en_US.utf8'
                                  ENCODING='UTF8'
                                  TEMPLATE=template0;
EOF

## process monitor (supervisor)
sudo apt-get install -y supervisor

## code-versioning (git)
sudo apt-get install -y git


#### python specifics
sudo apt-get install -y build-essential
sudo apt-get install -y ${PYTHON_VERSION}-setuptools

sudo apt-get install -y ${PYTHON_VERSION} ${PYTHON_VERSION}-dev

sudo apt-get install -y ${PYTHON_VERSION}-pip 
# replaced by in future Ubuntu LTS versions?
# ${PYTHON_VERSION} -m ensurepip --user


/usr/bin/${PYTHON_VERSION} -m pip install --user --upgrade pip
/usr/bin/${PYTHON_VERSION} -m pip install --user --upgrade virtualenv
/usr/bin/${PYTHON_VERSION} -m pip install --user --upgrade virtualenvwrapper

#BIN_VIRTUALENV=$HOME/.local/bin/virtualenv
BIN_VIRTUALENV=`find $HOME -name virtualenv -print -quit`

#BIN_VIRTUALENVWRAPPER=$HOME/.local/bin/virtualenvwrapper.sh
BIN_VIRTUALENVWRAPPER=`find $HOME -name virtualenvwrapper.sh -print -quit`

### Python Imaging Library (pillow, formerly PIL)
#sudo apt-get build-dep -y ${PYTHON_VERSION}-imaging


export VENVS="$HOME/.venvs"
export PROJECT_VENV="$VENVS/my_venv"
export PROJECT_HOME="/vagrant"
export PROJECT_REQUIREMENTS="${PROJECT_HOME}/requirements.txt"

if [ ! -f $HOME/virtualenv.sh ]; then
    cat <<EOT > $HOME/virtualenv.sh
#!/bin/bash
export WORKON_HOME=$VENVS
export PROJECT_HOME=$PROJECT_HOME
source ${BIN_VIRTUALENVWRAPPER}
EOT


    echo "source $HOME/virtualenv.sh" >> $HOME/.bashrc
    chmod u+x $HOME/virtualenv.sh
    chown vagrant:vagrant $HOME/virtualenv.sh
fi


### app-dependancies


if [ ! -f $PROJECT_VENV/bin/activate ]; then
    ${BIN_VIRTUALENV} $PROJECT_VENV --python ${PYTHON_VERSION} --always-copy
fi
$PROJECT_VENV/bin/python -m pip install --upgrade \
    --requirement $PROJECT_REQUIREMENTS
