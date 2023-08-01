#!/usr/bin/env bash

# Request IP from DHCP of external network
ip link set enp1s0 up
dhclient enp1s0

# Wait for DHCP to finish
sleep 10

# Generate Host Keys and restart sshd
cd /etc/ssh && ssh-keygen -A
systemctl restart sshd

# Resize disk to max space available
growpart /dev/vda 1
resize2fs /dev/vda1
