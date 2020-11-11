#!/bin/sh
read -p "which address do you want to scan? " address
echo "scanning $address"

nmap -p0- -v -A -T4 $address
