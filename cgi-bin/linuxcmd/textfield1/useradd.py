#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
username = mydata.getvalue("username")

#for top command
cmd = "sudo useradd {}".format(username)
output = subprocess.getoutput(cmd)

print(output
