#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
joomlavol = mydata.getvalue("mysqlvol")
JOOMLA_DB_HOST = mydata.getvalue("JOOMLA_DB_HOST")
JOOMLA_DB_USER = mydata.getvalue("JOOMLA_DB_USER")
JOOMLA_DB_PASSWORD = mydata.getvalue("JOOMLA_DB_PASSWORD")
JOOMLA_DB_NAME = mydata.getvalue("JOOMLA_DB_NAME")
name = mydata.getvalue("name")
image = mydata.getvalue("image")
version = mydata.getvalue("version")
port = mydata.getvalue("port")
#mysqlos = mydata.getvalue("mysqlos")

cmd1 = "sudo docker volume create {}".format(joomlavol)
output1 = subprocess.getoutput(cmd1)

cmd2 = "sudo docker run -dit -e JOOMLA_DB_HOST={} -e JOOMLA_DB_USER={} -e JOOMLA_DB_PASSWORD={} -e JOOMLA_DB_NAME={} -v {}:/var/www/html --name {} -p {}:80 --link {} {}:{}".format(JOOMLA_DB_HOST,JOOMLA_DB_USER,JOOMLA_DB_PASSWORD,JOOMLA_DB_NAME,joomlavol,name,port,JOOMLA_DB_HOST,image,version)
output2 = subprocess.getoutput(cmd2)

print(output2)
