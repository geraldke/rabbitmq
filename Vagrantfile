# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.define "rabbitmq" do |rabbitmq|
        rabbitmq.vm.box = "precise64"
        rabbitmq.vm.box_url = "http://files.vagrantup.com/precise64.box"
        rabbitmq.vm.provision :shell, :path => "bootstrap-rabbitmq.sh"
        rabbitmq.vm.network "public_network"
    end
end
