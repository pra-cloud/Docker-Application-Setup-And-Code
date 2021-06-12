#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

#for fdisk -l ( to know about the disk storage) command
output = subprocess.getoutput("sudo fdisk -l")

print(output)
