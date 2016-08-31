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

-   Run data creation command (`./manage.py insert_jobs`)

-   Run development server

        $ sudo /vagrant/.venvs/my_venv/bin/python /vagrant/jobzwo/manage.py runserver 0:80
        
-   Access http://dev.jobzwo.at/


Merge-Checklist
--------------

* Rebase/Merge on master branch.
* The vagrant setup is clean and works out of the box.
    * Also including automatic provisioning via bootstrap.sh.
    * Synchronize the README.md file to only include a minimal set of 
      instructions, not already present in the `vagrant-setup/provision.sh`.
* Check if migrations work.
    * run with an empty database (including fixtures).
    * run with current staging data-set.
* Ensure pep8-tool won't complain about your code.
  `pep8`
* Check the unit-tests (`manage.py test` must run without errors)
    * Include unit tests for all relevant code paths.
    * Make sure old unit-tests still work (manage.py test).
* check for `:TODO:` markers in your code and fix those.

