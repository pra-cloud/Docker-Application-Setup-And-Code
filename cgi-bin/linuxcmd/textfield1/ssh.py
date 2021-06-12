#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
hostip = mydata.getvalue("hostip")

#for top command
cmd = "sudo ssh {}".format(hostip)
output = subprocess.getoutput(cmd)

print(output)
