# Pentesting scripts
Some of these scripts are entirely mine, some belong entirely to others, and some are a mix of the two. I claim no credit for the development and implementation of these scripts, however they are stored in this repository for convenience.


## portscan.sh
Simple script which prompts user for a domain or IP address to run nmap with the following settings:

\n nmap -p0- -v -A -T4 $address
