#!/usr/bin/env python

import os
import json

inventory = {
    "_meta": {
        "hostvars": {
            "maas": {
                "ansible_host": os.environ.get("MAAS_EXTERNAL_IP"),
                "ansible_ssh_private_key_file": os.environ.get("MAAS_SSH_KEY"),
                "ansible_user": "root",
                "ansible_connection": "ssh",
            }
        }
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "maas"
        ]
    }
}

print(json.dumps(inventory))
