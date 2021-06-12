
#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
file1 = mydata.getvalue("file1")

cmd = "sudo wget {}".format(file1)
output = subprocess.getoutput(cmd)

print(output)

