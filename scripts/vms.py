#!/usr/bin/env python3

import libvirt
from xml.etree import ElementTree as ET

# Monitor nodes
conn = libvirt.open('qemu:///system')
domains = conn.listAllDomains()
for domain in domains:
    info = domain.info()
    domain_xml = domain.XMLDesc(0)
    domain_uuid = domain.UUIDString()

    # parse XML to get MAC address
    domain_et = ET.fromstring(domain_xml)
    mac_node = domain_et.find(".//devices/interface/mac")
    mac_address = mac_node.get('address') if mac_node is not None else 'No MAC address found'

    domain_info = {}
    domain_info[domain.name()] = {
        'state': info[0],
        'max_memory': info[1],
        'memory': info[2],
        'nr_virt_cpu': info[3],
        'cpu_time': info[4],
        'uuid': domain_uuid,
        'mac_address': mac_address
    }

    print(domain_info)
