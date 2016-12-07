# Script Name	: check_password.py
# Author	: Riley Young, Gangbiao Liu
# Created	: 25th November 2016
# Last Modified	:
# Version	: 1.01
# Modifications	:

# Description	:check remote host's (linux) weak password.

# Copyright (c) 2016 Gangbiao Liu.All rights reserved. 
# Permission to intall, use, copy, modify, and distribute this software for any
# but evil purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.

#-*- coding: utf-8 -*-
#!/usr/bin/python
import re, os, sys
import ConfigParser
import string
import paramiko

cf=ConfigParser.ConfigParser()
cf.read("test.conf")
port = cf.getint("hostn", "db_port")
username = cf.get("hostn", "db_user")

host_file=open("host.txt", "r")
host_lines=host_file.readlines()
host_counter=0

password_file=open("passwd.txt", "r")
password_lines = password_file.readlines()

print "\n\t......starting......"

for host_line in host_lines:
    password_counter = 0
    host_counter = host_counter+1
    host_line = host_line.strip()
    #password=line
    hostname = host_line
    print "\n\t Check IP：\t %s\n"%(hostname)
    for password_line in password_lines:
        password_counter = password_counter+1
        password_line = password_line.strip()
        password = password_line

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname,port,username,password)
            stdin, stdout, stderr = client.exec_command("pwd")
            #print stdout.read()
            print "password check [%d] : Success!\tweak passwd is：%s"%(password_counter,password)
            break
        except:
            print "password check [%d] : Failed!"%(password_counter)
        client.close()
password_file.close()
host_file.close()

print "\n\t......ending......\n"
