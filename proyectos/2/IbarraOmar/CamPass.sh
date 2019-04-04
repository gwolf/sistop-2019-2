#!/bin/bash
fun(){
if [ "`cut -d: -f1 /etc/shadow | egrep '^'$user'$'`" = "" ]
then
        echo No existe ese usuario
        exit
fi

echo Ingresa su nueva contrasena o x para salir
stty -echo
read contra1
if [ "$contra1" = "x" ]
then
       stty echo
	exit
fi
#verifica que es segura
if [ "$(echo $contra1|wc -m)" -ge "13" -a "$(echo $contra1|egrep '[0-9]')" -a "$(echo $contra1|egrep '[a-z]')" -a "$(echo $contra1|egrep '[A-Z]')" -a "$(echo $contra1|egrep '[#$%&.]')" ]
then
	if [ "$(echo $contra1 | egrep -o . | egrep -v '([0-9]|[a-z]|[A-Z]|[#$%&.])')" ]
	then
		echo Contrasena no valida
		sleep 2
		clear
		fun
	else
	        echo Ingresa nuevamente la contrasena
        	stty -echo
	        read contra2
        	stty echo
	        if [ "$contra1" = "$contra2" ]
        	then
	                PASS=$(echo $contra1 |mkpasswd -m sha-512 -s)
        	        usua=$(egrep '^'$user':' /etc/shadow)
                	#echo Usuario antes: $usua
	                nusua=$(echo $usua | cut -d: -f1):$PASS:$(echo $usua | cut -d: -f3-9)
        	        #echo Usuario ahora: $nusua
                	echo
	                sed 's@^'$user':.*$@'$nusua'@' /etc/shadow > SINUSUARIO
        	        cat SINUSUARIO > /etc/shadow
        	fi
	fi
else
        echo Tu contrasena no es segura
	sleep 2
	clear
	fun
fi
}


echo Ingresa el usuario del que deceas cambiar contrasena
read user
fun

