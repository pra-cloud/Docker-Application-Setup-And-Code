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

