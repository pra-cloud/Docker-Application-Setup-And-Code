#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

#for du -sh (to know about the memory used by current directory) command
output = subprocess.getoutput("sudo du -sh")

print(output)
