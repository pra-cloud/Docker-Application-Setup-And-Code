#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

#for last command
output = subprocess.getoutput("sudo last")

print(output)
