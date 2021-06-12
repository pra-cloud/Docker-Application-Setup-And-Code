
#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
file1 = mydata.getvalue("file1")
file2 = mydata.getvalue("file2")

cmd = "sudo mv {} {}".format(file1,file2)
output = subprocess.getoutput(cmd)

print(output)

