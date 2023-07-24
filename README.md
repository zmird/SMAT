SMAT - Simple MAAS AuTomation
=============================

Simple virtual laboratory to test automation written for MAAS.

Dependencies
------------

### Archlinux

Install libvirt and QEMU:

```sh
sudo pacman -S libvirt qemu-base
```

Make sure that the libvirtd deamon is running:

```sh
sudo systemctl start libvirtd
```

To ensure your user has access to the libvirt daemon, add it as a member to the `libvirt` group:
```sh
sudo usermod -a -G libvirt <username>
```

Install vagrant:

```sh
sudo pacman -S vagrant
```

Install the vagrant libvirt plugin:

```sh
vagrant plugin install vagrant-libvirt
```

Automation
----------

Playbooks:

- *maas.yml*: Installs and setups MAAS

- *libvirt.yml*: Creates the Virtual Machines and syncs them with MAAS

- *juju.yml*: Installs juju

Scripts:

- *libvirt-connector.py*: Provides a simple webhook interface to libvirt

- *env.sh*: Contains the environment variables needed

Prepare the Lab
---------------

Run the following command to prepare the lab environment

```sh
make
```

Activate the virtual environment:
```sh
source venv/bin/activate
```

Load the environment variables:

```sh
source scripts/env.sh
```


Create the Lab
--------------

Run the following command to create the MAAS virtual machine:

```sh
vagrant up --provider=libvirt
```

Start the Libvirt webhook connector
```sh
python scripts/libvirt-connector.py
```

Run the playbook to create the libvirt virtual machines:
```sh
ansible-playbook -i $VAGRANT_ANSIBLE_INVENTORY playbooks/libvirt.yml
```

Run the playbook to install juju
```sh
ansible-playbook -i $VAGRANT_ANSIBLE_INVENTORY playbooks/juju.yml
```
