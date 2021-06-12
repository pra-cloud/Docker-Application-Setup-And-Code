#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

#for ID command
output = subprocess.getoutput("sudo id")

print(output)
