#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
image = mydata.getvalue("image")
file1 = mydata.getvalue("file1")

cmd = "sudo docker save {} > {}".format(image,file1)
output = subprocess.getoutput(cmd)

print(output)
