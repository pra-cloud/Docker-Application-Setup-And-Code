#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
package = mydata.getvalue("package")

#for top command
cmd = "sudo yum info {} -y".format(package)
output = subprocess.getoutput(cmd)

print(output)
