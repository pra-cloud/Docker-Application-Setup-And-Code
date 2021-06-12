#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

#for df -h ( to know the memory & file history ) command
output = subprocess.getoutput("sudo df -h")

print(output)
