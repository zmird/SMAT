Role JuJu
=========

Installs and configures Juju.

Requirements
------------

A maas cloud on where to install JuJu.

Role Variables
--------------

The following variables could be used to customize the installation:

`juju_user` is the used used by juju
`juju_home` is the home where juju will create the config files

`maas_ip` is the MAAS IP
`maas_port` is the port used by MAAS
`maas_api_key` is the api key used by MAAS


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
- name: Install JUJU
  hosts: myhost
  become: true
  gather_facts: false
  tasks:
    - name: Import role_juju
      import_role:
        name: role_juju
      vars:
        role_juju_targets:
          - "install-juju"
```

License
-------

MIT
