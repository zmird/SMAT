#!/usr/bin/env python3

from flask import Flask, jsonify
import libvirt

app = Flask(__name__)


@app.route('/list', methods=['GET'])
def list():
    conn = libvirt.open("qemu:///system")
    if not conn:
        raise SystemExit("Failed to open connection to qemu:///system")

    # Get the list of active domain IDs
    active_ids = conn.listDomainsID()

    # Use the IDs to get the names of the active domains
    active_domains = [conn.lookupByID(id).name() for id in active_ids]

    # Get the names of the inactive domains
    inactive_domains = conn.listDefinedDomains()

    # Combine the lists
    all_domains = active_domains + inactive_domains

    return jsonify(all_domains)


@app.route('/start/<name>', methods=['POST'])
def start(name):
    conn = libvirt.open("qemu:///system")
    if not conn:
        raise SystemExit("Failed to open connection to qemu:///system")

    domain = conn.lookupByName(name)
    if not domain.isActive():
        domain.create()
    return f'Started VM {name}'


@app.route('/stop/<name>', methods=['POST'])
def stop(name):
    conn = libvirt.open("qemu:///system")
    if not conn:
        raise SystemExit("Failed to open connection to qemu:///system")

    domain = conn.lookupByName(name)
    domain.shutdown()
    return f'Stopped VM {name}'


@app.route('/status/<name>', methods=['GET'])
def status(name):
    conn = libvirt.open("qemu:///system")
    if not conn:
        raise SystemExit("Failed to open connection to qemu:///system")

    domain = conn.lookupByName(name)
    if domain.isActive():
        status = 'running'
    else:
        status = 'stopped'
    return jsonify({'status': status})


@app.route('/ready', methods=['GET'])
def ready():
    return "OK"


if __name__ == '__main__':
    app.run(host="192.168.121.1", port=5000)
