#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
#file1 = mydata.getvalue("top")

#for top command
cmd = "sudo df -h"
output = subprocess.getoutput(cmd)

print(output)
