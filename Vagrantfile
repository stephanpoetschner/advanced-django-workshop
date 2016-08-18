# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"  # LTS 14.04 (stick to LTS versions)
  config.vm.provision :shell, path: "vagrant-setup/provision.sh", privileged: false

  config.ssh.forward_agent = true

  config.vm.network :private_network, ip: '192.168.50.50'
  config.vm.synced_folder '.', '/vagrant'
  config.vm.synced_folder './.venvs', '/home/vagrant/.venvs'

  config.vm.provider "virtualbox" do |v|
    v.memory = 1972
  end

  # If a 'Vagrantfile.local' file exists, import any configuration settings
  # defined there into here. Vagrantfile.local is ignored in version control,
  # so this can be used to add configuration specific to this computer.
  if File.exist? "Vagrantfile.local"
    instance_eval File.read("Vagrantfile.local"), "Vagrantfile.local"
  end
  
end
