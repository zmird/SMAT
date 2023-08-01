SMAT - Simple MAAS AuTomation
=============================

Simple virtual laboratory to test automation written for MAAS.


                               |
                    eth0 +-----+
                               |
                               |   +------------------------------+
    +----------------------+   |   |                              |
    |                      |   |   |                  MAAS host   |
    |   192.168.122.0/24   |   |   |  10.0.0.0/24     10.0.0.2    |
    |   external           |   |   |  internal                    | 
    |                      |   |   |                  NODE-1 host |
    |             MAAS     |   |   |                  10.0.0.10   |
    |    192.168.122.2     |   +---+---+ virbr1                   |
    |                      |   |   |     10.0.0.1     NODE-2 host |
    |           virbr0 +---+---+   |                  10.0.0.11   |
    |    192.168.122.1     |   |   |                              |
    |                      |   |   |  libvirt DHCP off            |
    |                      |   |   |  MAAS DHCP on                |
    |  libvirt DHCP on     |   |   |                              |
    |                      |   |   +------------------------------+
    +----------------------+   |    
                               |

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

Prepare the Lab
---------------

Run the following command to prepare the lab environment

```sh
make all
```

Create the Lab
--------------

The necessary env vars needs to defined:

```sh
source scripts/env.sh
```

The following script can be used to create the lab

```sh
scripts/smat.sh --help
Usage: scripts/smat.sh [-h] [-l list-targets] [-a all] [-u uninstall] [-s setup-host] [-m install-maas] [-c configure-maas] [-n install-nodes] [-j install-juju]

Options:
-h, --help                Show help
-l, --list-targets        List all targets
-a, --all                 Execute all install and configure targets
-u, --uninstall           Execute the uninstall target
-s, --setup-host          Execute the setup-host target
-m, --install-maas        Execute the install-maas target
-c, --configure-maas      Execute the configure-maas target
-n, --install-nodes       Execute the install-nodes target
-j, --install-juju        Execute the install-juju target
    --uninstall-maas      Execute the uninstall-maas target
    --uninstall-nodes     Execute the uninstall-nodes target
    --uninstall-juju      Execute the uninstall-juju target
```

At some point during the nodes installation you will be asked to start the Libvirt webhook connector, to do it run:
```sh
python scripts/libvirt-connector.py
```

Automation
----------

Roles:

- *role_smat*: Contains the automation to install and configures MAAS and the virtual nodes 

- *role_juju*: Contains the automation to installs and configures JuJu

Playbooks:

- *smat.yml*: Installs and configures MAAS and the virtual nodes

- *juju.yml*: Installs and configures JuJu

Scripts:

- *smat.sh*: This script acts as an interface to the ansible automation, makes running it easier

- *libvirt-connector.py*: Provides a simple webhook interface to libvirt

- *env.sh*: Contains the environment variables needed

Inventories:

- *maas.py*: This ansible inventory only contains MAAS

- *libvirt.py*: This ansible inventory contains all the libvirt hosts
