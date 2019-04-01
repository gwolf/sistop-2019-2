#!/bin/bash
echo Ingresa tu contrasena
stty -echo 
read contra
stty echo
SAL=$(sudo grep ^`logname`: /etc/shadow | cut -d: -f2 | cut -d$ -f3)
if [ "$(echo $contra |mkpasswd -m sha-512 -s -S $SAL)" = $(sudo grep ^`logname`: /etc/shadow | cut -d: -f2) ]
then 
	R=0
else
	R=1
fi
