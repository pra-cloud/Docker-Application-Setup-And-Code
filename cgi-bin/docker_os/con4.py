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

if (networkname and vol and mount)==None:
        mount="/var"
        vol="test2"
        #print(vol)
        #print(mount)
        cmd2 = "sudo docker run -dit  --name {}  -p {}:{} {}:{}".format(name,port,defaultport,image,version)
        output2 = subprocess.getoutput(cmd2)
elif (vol and mount)==None:
        mount="/var"
        vol="test2"
        #print(vol)
        #print(mount)
        cmd3 = "sudo docker network create --driver bridge {}".format(networkname)
        output3 = subprocess.getoutput(cmd3)
        cmd2 = "sudo docker run -dit  --name {} --network {} -p {}:{} {}:{}".format(name,networkname,port,defaultport,image,version)
        output2 = subprocess.getoutput(cmd2)

elif ((networkname==None) and ((len(giturl)==0) or (len(giturl)!==0))) :
	cmd1 = "sudo docker volume create {}".format(vol)
        output1 = subprocess.getoutput(cmd1)
	if ((len(vol) !==0) and (len(giturl) !==0)):
			remove = subprocess.getoutput("sudo rm -frv /var/lib/docker/volumes/{}".format(vol))
			mkdir = subprocess.getoutput("sudo docker volume create {}".format(vol))
			print(giturl)
			git = subprocess.getoutput("sudo git clone {}  /var/lib/docker/volumes/{}/_data/".format(giturl,vol))
			print(git)
			print("Cloned!!!")
        cmd2 = "sudo docker run -dit -v {0}:{6} --name {1}  -p {2}:{3} {4}:{5}".format(vol,name,port,defaultport,image,version,mount)
        output2 = subprocess.getoutput(cmd2)

elif :
        cmd3 = "sudo docker network create --driver bridge {}".format(networkname)
        output3 = subprocess.getoutput(cmd3)
        cmd1 = "sudo docker volume create {}".format(vol)
        output1 = subprocess.getoutput(cmd1)
        cmd2 = "sudo docker run -dit -v {0}:{7} --name {1} --network {6} -p {2}:{3} {4}:{5}".format(vol,name,port,defaultport,image,version,networkname,mount)
        output2 = subprocess.getoutput(cmd2)

print(output2)

