Role SMAT
=========

Role used in the Small MAAS Automation repository.

Requirements
------------

Only Archlinux is supported at the moment.

The following software is needed to run the role:

- libvirt
- qemu

The following python packages are needed:

- libvirt-python
- lxml

Dependencies
------------

The following collections are needed:

- community.general
- community.libvirt
- containers.podman

Role Variables
--------------

The following variables can be changed to customize the automation:

`role_smat_targets` is a list strings containing the automation tasks to execute.
    - "host-setup"
    - "install-maas"
    - "configure-maas"
    - "install-nodes"
    - "uninstall-maas"
    - "uninstall-nodes"

`libvirt_user` is to define which user does the qemu emulator use to run.
`libvirt_group` is to define which group does the qemu emulator use to run.

`maas_nodes` is the number of nodes to create, excluding maas.

`maas_nodes_attr` is a dictionary which defines customizable attribute of nodes.
    - `memory` used by the node vm
    - `vcpus` used by the node vm

`maas_db` contains the information used to create the maas postgres database
    - `name`
    - `user`
    - `password`

`maas_admin` contains the credentials of the maas admin user
    - `username`
    - `password`
    - `email`


Example Playbook
----------------


Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
- name: Install MAAS
  hosts: localhost
  become: true
  gather_facts: false
  tasks:
    - name: Import role_smat
      import_role:
        name: role_smat
      vars:
        role_smat_targets: 
          - "install-maas"
          - "configure-maas"
```

License
-------

MIT
