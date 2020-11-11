#!/bin/sh
read -p "which address do you want to scan? " ip
echo "scanning $ip"

nmap -p0- -v -A -T4 $ip
