#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
name = mydata.getvalue("name")
newimage = mydata.getvalue("newimage")
version = mydata.getvalue("version")

cmd = "sudo docker commit {} {}:{}".format(name,newimage,version)
output = subprocess.getoutput(cmd)

print(output)
