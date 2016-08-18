Getting Started
---------------

-   Download and install Vagrant (https://www.vagrantup.com/downloads.html)

-   Add `192.168.50.50	dev.jobzwo.at` to hosts-file 
    (e.g. `/etc/hosts` on you LOCAL (!) linux machine)

-   Run `vagrant up`

-   Run `vagrant ssh` to connect to the development box and change directory to 
    `/vagrant` (`cd /vagrant`)

-   Activate virtualenv (`workon my_venv`)

-   Change directory to `/vagrant/jobzwo` (`cd /vagrant/jobzwo`)

-   Run migrations (`./manage.py migrate`)

-   Run development server

        $ sudo /vagrant/.venvs/my_venv/bin/python /vagrant/jobzwo/manage.py runserver 0:80
        
-   Access http://dev.jobzwo.at/
