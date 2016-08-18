Getting Started
---------------

-   Download and install Vagrant (https://www.vagrantup.com/downloads.html)

-   Add `192.168.50.50	dev.stephan-poetschner.at` to hosts-file 
    (e.g. `/etc/hosts` on you LOCAL (!) linux machine)

-   Run `vagrant up`

-   Run `vagrant ssh` to connect to the development box and change directory to 
    `/vagrant` (`cd /vagrant`)

-   Activate virtualenv (`workon my_venv`)

-   Change directory to `/vagrant` (`cd /vagrant/`)

-   Run migrations (`./manage.py migrations`)

-   Run development server

        $ sudo /vagrant/.venvs/my_venv/bin/python /vagrant/manage.py runserver 0:80
        
-   Access http://dev.stephan-poetschner.at/
