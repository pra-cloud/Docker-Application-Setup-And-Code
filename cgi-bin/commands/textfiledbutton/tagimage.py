#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
image = mydata.getvalue("image")
newimage = mydata.getvalue("newimage")

cmd = "sudo docker tag {} {}".format(image,newimage)
output = subprocess.getoutput(cmd)

print(output)
