# Pentesting scripts
Some of these scripts are entirely mine, some belong entirely to others, and some are a mix of the two. I claim no credit for the development and implementation of these scripts, however they are stored in this repository for convenience.


## portscan.sh
Simple script which prompts user for a domain or IP address to run nmap with the following settings:

nmap -p0- -v -A -T4 $address

## passwordgenerator.py
Python script that prompts a user for desired password length and requirements, as well as the desired filename for the password list.
A file is then generated with the entered filename (Be sure to specify file extension here) with every combination of the characters specified by the entered requirements up to the password length entered. For example:

  How many characters?
  2
  Enter 1 for lowercase letters.
  Enter 2 for numbers.
  Enter 3 for lower and uppercase letters.
  Enter 4 for alphanumeric lowercase.
  Enter 5 for alphanumeric with lower and uppercase.
  Enter 6 for lowercase with symbols.
  Enter 7 for lower and uppercase with symbols.
  Enter 8 for alphanumeric lowercase with symbols.
  Enter 9 for alphanumeric lower and uppercase with symbols.
  2
  Enter the file name:
  demo.txt
  
This will create a file demo.txt in the working directory with the following contents:

  0
  
  1
  
  2
  
  3
  4
  5
  6
  7
  8
  9
  00
  01
  02
  ...
  99
