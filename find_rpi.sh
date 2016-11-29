#!/bin/bash
# arp scan, greping the MAC address of the RPI itself and then the dongle
arp -a | grep b8:27:eb
arp -a | grep 3c:1e:04:81:a8:ca
# then try nmap looking for open SSH port
nmap -p 22 --open -sV 10.100.0.0/20
