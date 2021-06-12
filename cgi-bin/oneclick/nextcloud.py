#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
cloudvol = mydata.getvalue("mysqlvol")
NEXTCLOUD_DB_HOST = mydata.getvalue("NEXTCLOUD_DB_HOST")
NEXTCLOUD_DB_USER = mydata.getvalue("NEXTCLOUD_DB_USER")
NEXTCLOUD_DB_PASSWORD = mydata.getvalue("NEXTCLOUD_DB_PASSWORD")
NEXTCLOUD_DB_NAME = mydata.getvalue("NEXTCLOUD_DB_NAME")
name = mydata.getvalue("name")
image = mydata.getvalue("image")
version = mydata.getvalue("version")
port = mydata.getvalue("port")
#mysqlos = mydata.getvalue("mysqlos")

cmd1 = "sudo docker volume create {}".format(cloudvol)
output1 = subprocess.getoutput(cmd1)

cmd2 = "sudo docker run -dit -e NEXTCLOUD_DB_HOST={} -e NEXTCLOUD_DB_USER={} -e NEXTCLOUD_DB_PASSWORD={} -e NEXTCLOUD_DB_NAME={} -v {}:/var/www/html --name {} -p {}:80 --link {} {}:{}".format(NEXTCLOUD_DB_HOST,NEXTCLOUD_DB_USER,NEXTCLOUD_DB_PASSWORD,NEXTCLOUD_DB_NAME,cloudvol,name,port,NEXTCLOUD_DB_HOST,image,version)
output2 = subprocess.getoutput(cmd2)

print(output2)
