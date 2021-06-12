#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
vol = mydata.getvalue("vol")
name = mydata.getvalue("name")
image = mydata.getvalue("image")
version = mydata.getvalue("version")
port = mydata.getvalue("port")
defaultport = mydata.getvalue("defaultport")
networkname = mydata.getvalue("networkname")
mount = mydata.getvalue("mount")
giturl = mydata.getvalue("giturl")


if giturl:
        cmd3 = "sudo docker network create --driver bridge {}".format(networkname)
        output3 = subprocess.getoutput(cmd3)
        print("your networkname is:" + networkname)
        remove = subprocess.getoutput("sudo rm -frv /var/lib/docker/volumes/{}".format(vol))
        mkdir = subprocess.getoutput("sudo docker volume create {}".format(vol))
        print("your volume name is:" + vol)
        git = subprocess.getoutput("sudo git clone {}  /var/lib/docker/volumes/{}/_data/".format(giturl,vol))
        print("your github repo URL is:" + git)
        print("Cloned!!!")
        cmd2 = "sudo docker run -dit -v {0}:{7} --name {1} --network {6} -p {2}:{3} {4}:{5}".format(vol,name,port,defaultport,image,version,networkname,mount)
        output2 = subprocess.getoutput(cmd2)
        print("your container id is:" + output2)
else:
   print("Invalid Option")
