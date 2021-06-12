#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
drupalvol = mydata.getvalue("mysqlvol")
DRUPAL_DB_HOST = mydata.getvalue("DRUPAL_DB_HOST")
DRUPAL_DB_USER = mydata.getvalue("DRUPAL_DB_USER")
DRUPAL_DB_PASSWORD = mydata.getvalue("DRUPAL_DB_PASSWORD")
DRUPAL_DB_NAME = mydata.getvalue("DRUPAL_DB_NAME")
name = mydata.getvalue("name")
image = mydata.getvalue("image")
version = mydata.getvalue("version")
port = mydata.getvalue("port")
#mysqlos = mydata.getvalue("mysqlos")

cmd1 = "sudo docker volume create {}".format(drupalvol)
output1 = subprocess.getoutput(cmd1)

cmd2 = "sudo docker run -dit -e DRUPAL_DB_HOST={} -e DRUPAL_DB_USER={} -e DRUPAL_DB_PASSWORD={} -e DRUPAL_DB_NAME={} -v {}:/var/www/html --name {} -p {}:80 --link {} {}:{}".format(DRUPAL_DB_HOST,DRUPAL_DB_USER,DRUPAL_DB_PASSWORD,DRUPAL_DB_NAME,drupalvol,name,port,DRUPAL_DB_HOST,image,version)
output2 = subprocess.getoutput(cmd2)

print(output2)
