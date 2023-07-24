# -*- mode: ruby -*-
# vi: set ft=ruby :

BOX       = "generic/ubuntu2204"
NODES     = 2

Vagrant.configure("2") do |config|

  config.vm.box = BOX

  config.vm.provider :libvirt do |libvirt|
    libvirt.driver = "kvm"
    libvirt.host = "localhost"
    libvirt.uri = "qemu:///system"
    libvirt.qemu_use_session = false
    libvirt.cpus = 2
    libvirt.memory = 2048
    libvirt.management_network_address = "192.168.121.0/24"
  end

  # MAAS
  config.vm.define "maas" do |maas|
    maas.vm.hostname = "maas"

    maas.vm.network :private_network, 
      :ip => "192.168.121.10"

    maas.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbooks/maas.yml"
      ansible.compatibility_mode = "2.0"
    end
  end
end

