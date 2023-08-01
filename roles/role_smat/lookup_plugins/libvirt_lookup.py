import libvirt
from ansible.plugins.lookup import LookupBase
from xml.etree import ElementTree as ET


class LookupModule(LookupBase):
    def get_vm_info(self, name, network):
        domain = self.conn.lookupByName(name)

        info = domain.info()
        domain_xml = domain.XMLDesc(0)
        domain_uuid = domain.UUIDString()

        # parse XML to get MAC address
        domain_et = ET.fromstring(domain_xml)
        mac_node = domain_et.find(".//devices/interface/mac")
        mac_address = mac_node.get('address') if mac_node is not None else None

        # Get IP addresses associated with the vm
        ips = []
        leases = self.conn.networkLookupByName(network).DHCPLeases()
        for lease in leases:
            if lease['mac'] == mac_address:
                ips.append(lease['ipaddr'])

        return {
            'name': domain.name(),
            'state': info[0],
            'max_memory': info[1],
            'memory': info[2],
            'vcpus': info[3],
            'uuid': domain_uuid,
            'mac_address': mac_address,
            'ips': ips
        }
    
    def run(self, terms, variables=None, **kwargs):
        self.conn = libvirt.open('qemu:///system')

        vms_list = kwargs.get('vms', [])
        network_name = kwargs.get('network', None)

        if network_name is None:
            # raise error
            pass

        if len(vms_list) == 0:
            # raise error
            pass

        if len(vms_list) == 1:
            domain_info = self.get_vm_info(vms_list[0], network_name)
            return domain_info

        domains = self.conn.listAllDomains()
        result = []
        for domain in domains:
            if domain.name() not in vms_list:
                continue

            domain_info = self.get_vm_info(domain.name(), network_name)
            result.append(domain_info)

        return result
