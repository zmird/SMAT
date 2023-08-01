#!/usr/bin/env python3

import os
import json
import libvirt
from xml.etree import ElementTree as ET


def get_domain_ip(conn, name):
    domain = conn.lookupByName(name)
    domain_xml = domain.XMLDesc(0)

    # parse XML to get MAC address
    domain_et = ET.fromstring(domain_xml)
    mac_node = domain_et.find(".//devices/interface/mac")
    mac_address = mac_node.get('address') if mac_node is not None else None

    # Get IP addresses associated with the vm
    leases = conn.networkLookupByName('maas-external').DHCPLeases()
    for lease in leases:
        if lease['mac'] == mac_address:
            return lease['ipaddr']

    return None


def get_active_domains() -> dict:
    conn = libvirt.open('qemu:///system')
    if conn is None:
        print('Failed to open connection to qemu:///system')
        return {}

    domainIDs = conn.listDomainsID()
    domains = {}
    if not domainIDs:
        print('Failed to get a list of domain IDs')
    else:
        for domainID in domainIDs:
            dom = conn.lookupByID(domainID)
            dom_ip = get_domain_ip(conn, dom.name())
            if dom_ip:
                domains[dom.name()] = {
                    "ansible_host": dom_ip,
                    "ansible_ssh_private_key_file": os.environ.get("MAAS_SSH_KEY"),
                    "ansible_user": "root",
                    "ansible_connection": "ssh",
                    "host_key_checking": False,
                }

    conn.close()
    return domains


hosts = get_active_domains()

inventory = {
    "_meta": {
        "hostvars": hosts
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": list(hosts.keys())
    }
}

print(json.dumps(inventory))
