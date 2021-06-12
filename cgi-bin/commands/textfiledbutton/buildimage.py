#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
image = mydata.getvalue("image")
directory = mydata.getvalue("directory")

cmd = "sudo docker build -t {} {}".format(image,directory)
output = subprocess.getoutput(cmd)

print(output)
