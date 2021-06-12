#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

#for ps command
output = subprocess.getoutput("sudo ps")

print(output)
