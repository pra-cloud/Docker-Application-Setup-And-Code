
#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
directory = mydata.getvalue("directory")

cmd = "sudo mkdir {}".format(directory)
output = subprocess.getoutput(cmd)

print(output)

