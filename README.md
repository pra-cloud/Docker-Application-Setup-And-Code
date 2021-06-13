# Docker-Application-Setup-And-ServerCode

#install httpd and enable
yum install httpd
systemctl enable httpd
systemctl start httpd

#install docker and enable
yum install docker 
systemctl enable docker
systemctl start docker

#disable selinux

setenforce 0

#give permission to root user and httpd  in /etc/suoders file

vim /etc/sudoers
root    ALL=(ALL)       ALL

apache  ALL=(ALL)      NOPASSWD: ALL

#put all files and folder inside /var/www/cgi-bin location

cd /var/www/cgi-bin

#give permission of read and write to the all files

chmod +x *

