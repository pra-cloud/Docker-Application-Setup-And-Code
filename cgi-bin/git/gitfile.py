#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
giturl = mydata.getvalue("giturl")
vol = mydata.getvalue("vol")


remove = subprocess.getoutput("sudo rm -f /root/git/{}".format(vol))
mkdir = subprocess.getoutput("sudo mkdir /root/git/{}".format(vol))
print("your directory name is:" + vol)

git = subprocess.getoutput("sudo git clone {}  /root/git/{}".format(giturl,vol))
print("your GitHub repo URL is:" + git)
