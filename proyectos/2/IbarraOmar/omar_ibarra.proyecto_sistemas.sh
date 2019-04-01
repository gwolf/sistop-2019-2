#!/bin/bash
MENU(){
	clear
	echo '\***************PROYECTO*************/'
	echo "Selecciona alguna de las siguientes opciones"
	echo "1.- Administracion"
	echo "2.- Operaciones basicas"
	echo "3.- Operaciones sobre archivos"
	echo "4.- Informacion general"
	echo "5.- Salir"
	read opc
}

MENUADMIN(){
	clear
	echo '\******************ADMINISTRACION**************/'
	echo "Selecciona alguna de las siguientes opciones:"
	echo "1.- Monitoreo"
	echo "2.- Gestion de usuarios"
	echo "3.- Gestion de procesos"
	echo "4.- Respaldos"
	echo "5.- Regresar a menu principal"
	read opc
}

MENUMONITOREO(){
	clear
	echo '\******************MONITOREO**************/'
	echo "Selecciona alguna de las siguientes opciones:"
	echo "1.- Disco"
	echo "2.- Memoria"
	echo "3.- Carga del sistema"
	echo "4.- Usuarios"
	echo "5.- Regresar a menu principal"
	read opc
}

MENUGESTION(){
	clear
	echo '\******************GESTION DE USUARIOS**************/'
	echo "Selecciona alguna de las siguientes opciones:"
	echo "1.- Informacion sobre algun usuario"
	echo "2.- Cambio de password"
	echo "3.- Regresar a menu principal"
	read opc
}

MENURESPALDOS(){
	clear
        echo '\******************RESPALDOS**************/'
        echo "Selecciona alguna de las siguientes opciones:"
        echo "1.- Respaldo completo"
        echo "2.- Respaldo incremental"
        echo "3.- Respaldo diferencial"
	echo "4.- Resgresar al menu principal"
        read opc
}


MENUOPERACIONESBASIC(){
	clear
	echo '\******************OPERACIONES BASICAS**************/'
	echo "Selecciona alguna de las siguientes opciones:"
	echo "1.- mv "
	echo "2.- cp"
	echo "3.- find"
	echo "4.- mkdir"
	echo "5.- cron"
	echo "6.- Regresar a menu principal"
	read opc
}

MENUOPERACIONESARCHIVOS(){
	clear
        echo '\******************OPERACIONES SOBRE ARCHIVOS**************/'
        echo "Selecciona alguna de las siguientes opciones:"
        echo "1.- Archivos duplicados"
        echo "2.- Cifrado"
        echo "3.- Regresar a menu principal"
        read opc
}


MENUINFO(){
	clear
	echo '\******************INFORMACION GENERAL********************/'
	echo "Selecciona alguna de las siguientes opciones:"
	echo "1.- Usuarios conectados"
	echo "2.- Tiempo arriba"
	echo "3.- Regresar a menu principal"
	read opc
}

SALIR(){
	echo Oprime x para salir o cualquier otra tecla seguida de un enter para regresar al menu principal
	read option
	if [ "$option" = "x" ]
	then	
		exit
	else 
		CASOS
	fi
}
CASOS(){
	#AQUI SE HACE LA LECTURA DE LA OPCION QUE INGRESA EL USUARIO
        MENU
        case "$opc" in
        1)
		#REVISA SI ERES EL USUARIO ROOT Y SI NO NO TE DEJA ENTRAR EN ESTA OPCION
		if [ `echo $UID` != "0" ]
		then
			echo "Para entrar a esta opcion necesitas ser root"
			sleep 3
			clear
			CASOS

		fi
		#SE HACE LECTURA DE LA OPCION QUE INGRESA EL USUARIO EN EL MENU DE ADMINISTRACION
                MENUADMIN
		case "$opc" in
	        1)
			#SE HACE LECTURA DE LA OPCION QUE INGRESA EL USUARIO EN EL MENU DE MONITOREO
        	        MENUMONITOREO
			case "$opc" in
	                1)
                	        #disco
				echo "`logname` ingreso a ver el disco el `date +"%D a las %H:%M:%S"`">>./bitacora.log
				#SE CHECA EL ESPACIO DISPONIBLE EN EL DISCO, EL DISCO  EL ESPACIO TOTAL
				watch -n 1 . ./disco.sh
				clear
				CASOS
				;;
	                2)
                	        #memoria
				echo "`logname` ingreso a ver la memoria el `date +"%D a las %H:%M:%S"`">>./bitacora.log
				#SE CHECA LA MEMORIA
				watch -n 1 . ./memoria.sh
				clear
				CASOS
				;;
	                3)
                	        #carga del sistema
				echo "`logname` ingreso a ver la carga del sistema el `date +"%D a las %H:%M:%S"`">>./bitacora.log
				#SE REVISA LA CARGA DEL SISTEMA
				watch -n 1  . ./cargadelsistema.sh
				clear
				CASOS
				;;
	                4)
        	                #usuarios
				echo "`logname` ingreso a ver los usuarios el `date +"%D a las %H:%M:%S"`">>./bitacora.log
				#SE MIESTRA A LOS USUARIOS CONECTADOS
				watch -n 1 . ./usuarios.sh
	                        clear
				CASOS
				;;
                	5)
        	                CASOS;;
	                *)
                	        echo $opc no es una opcion del menu, por favor ingesa una opcion del menu
        	                echo "`logname` ingreso una opcion no valida al menu el `date +"%D a las %H:%M:%S"`">>./bitacora.log
	                        MENUMONITOREO
                	esac;;
	        2)
        	        MENUGESTION
			case "$opc" in
        	        1)
	                        #info de usuario
				echo "`logname` ingreso a ver informacion de los usuarios el `date +"%D a las %H:%M:%S"`">>./bitacora.log
				#SE MOSTRARA INFORMACION A CERCA DEL USUARIO INGRESADO
				echo Ingresa el nombre del usuario del que deceas informacion: 
				read user
				while [ "`cut -d: -f1 /etc/passwd | egrep ^$user$`" = "" ]
				do
					echo "El usuario no existe, ingresa otro: "
					read user
				done
					echo "`egrep ^$user: /etc/passwd`"|awk 'BEGIN{
					FS=":"}
					{
				        printf "Usuario: "$1"\nIdentificador de usuario: "$3"\nIdentificador de grupo: "$4"\nGECOS: "$5"\nHOME: "$6"\nSHELL: "$7"\n\n"
					print "*********************************************"}'
				SALIR
				;;
                	2)
        	                #cambio de password
				#AQUI SE PUEDE CAMBIAR EL PASSWORD 
				echo "`logname` ingreso a cambiar el password de alguien el `date +"%D a las %H:%M:%S"`">>./bitacora.log
				. ./CamPass.sh

	                        SALIR;;
                	3)
        	                CASOS
	                        ;;
			*)
				echo $opc no es una opcion del menu, por favor ingesa una opcion del menu
                        	echo "`logname` ingreso una opcion no valida al menu el `date +"%D a las %H:%M:%S"`">>./bitacora.log
                       		MENUGESTION
            		esac;;

		3)
			#gestionP
			echo "`logname` ingreso gestion de procesos el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			#AQUI SE MUESTRAN LOS PROCESOS QUE SE ESTAN EJECUTANDO EN ESE MOEMENTO Y MUESTRA ALGUNAS SEÑALES QUE SE LE PUEDEN ENVIAR
			ps ax | tr -s [:blank:]  |awk '
                                        {
                                        printf "Identificador: "$1"\tNombre del Proceso: "$5"\n"
                                        print "*********************************************"}'
			echo "Quieres enviar una senal a algun proceso?[s/n]"
			read op
			if [ "$op" = "s" ]
			then	
				echo "19.-SigStop"
				echo "18.-SigCont"
				echo "15.-SigTerm"
				echo "9.-SigKill"
				echo "Que senal deceas enviar?"
				read senal
				while [ `echo "$senal" | egrep -v '^(19|18|15|9)$'` ]	
				do
					echo No existe esa opcion, ingresa otra:
					read senal
					conta=$(expr $conta + 1)
					if [ "$conta" -eq "3" ]
        	                        then
                	                        echo Demasiados intentos
                        	                exit
                                	fi
				done	 
				conta=0
				echo "Ingresa el identificador del proceso al que deceas enviar esa senal: "
                                read pros
                                while [ "`ps ax | cut -d" " -f2 | egrep $pros`" = "" ]      
                                do
                                        echo No existe ese proceso, ingresa otro:
                                        read pros
                                        conta=$(expr $conta + 1)
                                        if [ "$conta" -eq "3" ]
                                        then
                                                echo Demasiados intentos
                                                exit
                                        fi
                                done
			
				kill -$senal $pros
				echo Se envio la senal correctamente
			fi
			SALIR
			;;
	        4)
			MENURESPALDOS
			#EN TODA ESTA SECCION SE REALIZAN RESPALDOS (COMPLETOS, DIFERENCIALES O INCREMENTALES)
			case "$opc" in
                        1)
                                #completo
				echo "`logname` ingreso a hacer un respaldo completo el `date +"%D a las %H:%M:%S"`">>./bitacora.log
				echo Que archivo deceas empaquetar?
				read archi
				test -r "$archi"
				nu=0
	                        while [ "$?" -ne "0" -a "$nu" -lt "3" ]
        	                do
                	                echo Ese archivo no existe, ingresa un archivo que exista
                        	        read cop
	                                nu=$(expr 1 + $nu)
                                	test -r $cop
        	                done
					if [ "$nu" -eq "3" ]
        	                then
                	                echo Desmasiados intentos 
                        	        sleep 2
                                	CASOS
	                        else
        	                        echo Ingresa el nuevo nombre del empaquetado
                	                read emp
					echo Empaquetando:
                        	        tar -cvzf $emp  $archi  2>>errores.log
                       		fi
                                SALIR
				;;
                        2)
                                #incremental
				echo "`logname` ingreso a hacer un respaldo incremental el `date +"%D a las %H:%M:%S"`">>./bitacora.log
				echo Que archivo deceas empaquetar?
                                read archi
				nu=0
                                test -r $archi
                                while [ "$?" -ne "0" -a "$nu" -lt "3" ]
                                do
                                        echo Ese archivo no existe, ingresa un archivo que exista
                                        read cop
                                        nu=$(expr 1 + $nu)
                                        test -r $cop
                                done
                                        if [ "$nu" -eq "3" ]
                                then
                                        echo Desmasiados intentos 
                                        sleep 2
                                        CASOS
                                else
                                        echo Ingresa el nuevo nombre del empaquetado
                                        read emp
                                        rsync -vax --progress  $archi $emp   2>>errores.log
                                fi
				SALIR
                                ;;
			3)
				#diferencial
				echo "`logname` ingreso a hacer un respaldo diferencial el `date +"%D a las %H:%M:%S"`">>./bitacora.log
				echo Que archivo deceas empaquetar?
                                read archi
				nu=0
                                test -r $archi
                                while [ "$?" -ne "0" -a "$nu" -lt "3" ]
                                do
                                        echo Ese archivo no existe, ingresa un archivo que exista
                                        read cop
                                        nu=$(expr 1 + $nu)
                                        test -r $cop
                                done
                                        if [ "$nu" -eq "3" ]
                                then
                                        echo Desmasiados intentos 
                                        sleep 2
                                        CASOS
                                else
                                        echo Ingresa el nuevo nombre del empaquetado
                                        read emp
                                        rsync -vax --progress  $archi $emp  2>>errores.log
                                fi
				SALIR
				;;
			4)
                                CASOS
                                ;;
                        *)
                                echo $opc no es una opcion del menu, por favor ingesa una opcion del menu
                                echo "`logname` ingreso una opcion no valida al menu el `date +"%D a las %H:%M:%S"`">>./bitacora.log
                                MENURESPALDOS
                        esac;;
	        5)
        	        CASOS;;
	        *)
        	        echo $opc no es una opcion del menu, por favor ingesa una opcion del menu
        	        echo "`logname` ingreso una opcion no valida al menu el `date +"%D a las %H:%M:%S"`">>./bitacora.log
                	MENUADMIN
		esac;;
        2)
		MENUOPERACIONESBASIC
		#EN ESTA SECCION SE REALIZAN ALGUNOS COMANDOS BASICOS DE GNU/LINUX
		case "$opc" in
	        1)
	                #mv
			echo "`logname` ingreso a hacer un mv el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			echo Ingresa el nombre del archivo a renombrar
			read nomv
			nu=0
			test -r $nomv
			while [ "$?" -ne "0" -a "$nu" -lt "3" ]
			do
				echo Ese archivo no existe, ingresa un archivo que exista 
			        read nomv
				nu=$(expr 1 + $nu)
				test -r $nomv
			done	

			if [ "$nu" -eq "3" ]
			then
				echo Desmasiados intentos 
				sleep 2
				CASOS
			else
				echo Ingresa el nuevo nombre
				read nomn
				mv $nomv $nomn 2>>errores.log
			fi
			SALIR
			;;
	        2)
	                #cp
			echo "`logname` ingreso a hacer un cp el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			echo Ingresa el nombre del archivo a copiar
                        read cop
                        nu=0
			if [ -r $cop ]
			then
			       	test -r $cop
        	                while [ "$?" -ne "0" -a "$nu" -lt "3" ]
                	        do
                        	        echo Ese archivo no existe, ingresa un archivo que exista
                                	read cop
	                                nu=$(expr 1 + $nu)
        	                        test -r $cop
                	        done
	
        	                if [ "$nu" -eq "3" ]
                	        then
                        	        echo Desmasiados intentos
                                	sleep 2
	                                CASOS
        	                else
                	                echo Ingresa el nombre de la copia
                        	        read ncop	
                               		cp -r $cop $ncop 2>>errores.log
	                        fi
			else
				echo El directorio en el que se encuentra no tiene el permiso de lectura, lo siento.
				sleep 2
				CASOS
			fi
			SALIR
			;;
	        3)
			#find
			echo "`logname` ingreso a hacer un find el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			echo Ingresa el nombre del archivo a buscar
			read bus
			echo Ingresa en donde queires buscar
			read lugar
			clear
			echo Resultado de busqueda: 
			find $lugar -name $bus 2>>errores.log
			SALIR
			;;
	        4)
        	        #mkdir
			echo "`logname` ingreso a hacer un mkdir el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			echo Ingresa el nombre del directorio que deceas crear
			read dire
			mkdir -p $dire
			SALIR
			;;
		5)
			#cron
			#min, horas, diames, mes, diasemana
			echo "`logname` ingreso a hacer un cron el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			echo "Ingresa cada cuanto tiempo quieres que se repita (minutos horas diadelmes mes diasemana)"
			read tiempo
			if [ "$(echo "$tiempo" | egrep '(^(([0-5]*[0-9])((-|,)[0-5]*[0-9])*|\*) (([0-1]*[0-9]|2[0-4])((-|,)[0-1]*[0-9]|-2[0-4])*|\*) (([1-9]|[12][0-9]|3[01])((-|,)[1-9]|[12][0-9]|-3[01])*|\*) (([1-9]|1[0-2])((-|,)[1-9]|-1[0-2])*|\*) ((([0-6])((-|,)[0-6])*)|\*)$)|^\*/[0-9]+ \*/[0-9]+ \*/[0-9]+ \*/[0-9]+ \*/[0-9]+$)')" ]
			then
				echo Ingresa el comando a ejecutar
				read comand
				echo "$tiempo" "$comand" | crontab
			else
				echo Argumentos no validos
				CASOS
			fi
			SALIR
			;;	
	        6)
                	CASOS;;
	        *)
        	        echo $opc no es una opcion del menu, por favor ingesa una opcion del menu
	                echo "`logname` ingreso una opcion no valida al menu el `date +"%D a las %H:%M:%S"`">>./bitacora.log
                	MENUOPERACIONESBASIC

        		esac
			;;
        3)
		MENUOPERACIONESARCHIVOS
		case "$opc" in
                1)
                        #archivos repetidos
			echo "`logname` ingreso a ver archivos repetidos el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			#ESTA PARTE AYUDA A BUSCAR SI SE TIENE ALGUN ARCHIVO REPETIDO EN ALGUNA RUTA QUE SE LE INDIQUE
			echo "Ingresa la ruta del directorio que deceas ver si tiene archivos con contenido repetido"
			read ruta
			test -d $ruta
			if [ $? -eq 0 ]
			then
				>temp
				gu=IFS
				IFS=$'\n'
				for var in `find $ruta`
				do
					test -d $var
					if [ $? -ne 0 ]
					then
       						sha512sum $var >>temp
					fi
				done
				IFS=$gu
				for nor in `sort temp | cut -d' ' -f1 | uniq -u`
				do
        				sed '/'$nor'/d' ./temp>temp2
        				cat temp2 > temp
				done
				if [ "`cat temp`" != '' ]
				then
					echo Los siguientes archivos son iguales en contenido
					for rep in `cut -d' ' -f1 temp | sort -u`
					do
        					egrep $rep temp | cut -d' ' -f3
        					echo '***********************************************'
					done
				else 
					echo "No hay archivos repetidos"
				fi
			else 
				echo No es un directorio
			fi
			SALIR
                        ;;
                2)
                        #cifrado
			echo "`logname` ingreso a hacer un cifrado el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			clear
			#SE CIFRAN ARCHIVOS CON EL COMANDO gpg
			echo 'Ingresa el nombre del archivo que deceas cifrar'
			read ar
			clear
			test -r $ar
			while [ "$?" -ne 0 ]
			do 
				echo No existe ese archivo o no tiene permiso de lectura, ingresa otro por favor
				read ar
				clear
			done	
			while [ -d $ar ]
			do
				echo Es un directorio, por favor ingresa un archivo
				read ar
				clear
			done


			while [ -r $ar.gpg ]
                        do
                                echo Ya existe ese archivo cifrado, ingresa otro por favor
                                read ar
                                clear
                        done

			echo "Ingresa una contrasena segura (13 caracteres, al menos un numero, una letra minuscula, una mayuscula, y dos simbolos (#$%&.))"
			stty -echo
			read contra
			clear
			if [ "$(echo $contra|wc -m)" -ge "13" -a "$(echo $contra|egrep '[0-9]')" -a "$(echo $contra|egrep '[a-z]')" -a "$(echo $contra|egrep '[A-Z]')" -a "$(echo $contra|egrep '[#$%&.]')" ]
			then
        			if [ "$(echo $contra | egrep -o . | egrep -v '([0-9]|[a-z]|[A-Z]|[#$%&.])')" ]
        			then
                		echo Contrasena no valida
				CASOS
				else
					if [ "$(echo $contra | wc -c)" -ge "13" ]
					then
						echo "Ingresa nuevamente la contrasena"
						stty -echo
						read contra2
						stty echo
						if [ "$contra" = "$contra2" ]
						then
							echo $contra| gpg --batch -c --passphrase-fd 0 $ar  2>>errores.log
						else
							echo Las contrasenas no coinciden
							CASOS
						fi
	
					fi
				fi
			else
				echo Contrasena no valida
				CASOS
			fi
				echo ""
                        SALIR
			;;
                3)
                        CASOS
                        ;;
                *)
                        echo $opc no es una opcion del menu, por favor ingesa una opcion del menu
                	echo "`logname` ingreso una opcion no valida al menu el `date +"%D a las %H:%M:%S"`">>./bitacora.log
                MENUOPERACIONESARCHIVOS
                esac
		;;
        4)
		MENUINFO
		case "$opc" in
	        1)
	                #usuariosconectados
			echo "`logname` ingreso a ver los usuarios conectados el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			clear
			#AQUI SE MUESTRAN A LOS USUSARIOS CONECTADOS Y ALGUNOS DATOS REELEVANTES DE ESTE
			for var in $(w -h | cut -d' ' -f1)
                        do
				echo "Usuario: $var"
				echo "Terminal: $(w -h $var | tr -s [:blank:] | tr -d : | cut -d' ' -f2)"
				echo "Nodo remoto: $(w -h $var | tr -s [:blank:] | tr -d : | cut -d' ' -f3)"
				echo "Tiempo de conexion:  $(w -h $var | tr -s [:blank:] | cut -d' ' -f4)"  
				echo "Tiempo inactivo: $(w -h $var | tr -s [:blank:] | cut -d' ' -f5)"
				echo "JCPU: $(w -h $var | tr -s [:blank:] | cut -d' ' -f6)"
				echo "PCPU: $(w -h $var | tr -s [:blank:] | cut -d' ' -f7)"
		      	done
			SALIR
			;;
        	2)
	                #tiempo arriba
			echo "`logname` ingreso a ver el tiempo que lleva arriva la maquina el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			clear
			#AQUI SE MUESTRA EL TIEMPO QUE LLEVA ARRIVA LA MAQUINA 
			echo Tiempo arriba: $(uptime | tr ',' / | cut -d/ -f1 | egrep -o 'up .*' |tr -d 'up ')
			SALIR
			;;
		3)
      	        	CASOS
			;;
	        *)
        	        echo $opc no es una opcion del menu, por favor ingesa una opcion del menu
       	         echo "`logname` ingreso una opcion no valida al menu el `date +"%D a las %H:%M:%S"`">>./bitacora.log
       	         MENUINFO
	        esac
		;;
        5)
                echo "Hasta luego :)"
                exit;;
        *)
                echo $opc no es una opcion del menu, por favor ingesa una opcion del menu
                echo "`logname` ingreso una opcion no valida al menu el `date +"%D a las %H:%M:%S"`">>./bitacora.log
                CASOS

        esac
}
. ./autorizacion.sh
if [ "$R" = "1" ]
then
	echo "Contrasena incorrecta, adios :)"
	exit
fi

if [ "$#" -eq "0" ]
then
	echo "`logname` ingreso al modo interactivo el `date +"%D a las %H:%M:%S"`">>./bitacora.log
	CASOS
elif [ "$#" -eq 1 -a "$1" = "--man" ]
then
	more manual
elif [ "$1" = "-A" ]
then
	if [ "`echo $UID`" != "0" ]
        then
		echo "`logname` no ingreso correctamente la contrasena `date +"%D a las %H:%M:%S"`">>./bitacora.log
                echo "Para entrar a esta opcion necesitas ser root"
                exit
        fi
	if [ "$2" = "-M" -a "$#" -eq "3" ]
	then
		if [ "$3" = "-D" ]
		then
			echo "`logname` ingreso a ver el disco el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			watch -n 1 . ./disco.sh
		elif [ "$3" = "-M" ]
		then
			echo "`logname` ingreso a ver la memoria el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			watch -n 1 . ./memoria.sh
		elif [ "$3" = "-CS" ]
		then
			echo "`logname` ingreso a ver la carga del sistema el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			watch -n 1  . ./cargadelsistema.sh
		elif [ "$3" = "-U" ]
		then
			echo "`logname` ingreso a ver los usuarios el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			watch -n 1 . ./usuarios.sh
		else
			echo Argmento no valido
		fi
	elif [ "$2" = "-GU" -a "$#" -eq "3" ]
	then
		if [ "$3" = "-I" ]
                then
			echo "`logname` ingreso a ver informacion de algun usuario el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			echo Ingresa el nombre del usuario del que deceas informacion:
			read user
			if [ "`cut -d: -f1 /etc/passwd | egrep ^$user$`" = "" ]
			then
				echo "El usuario no existe"
				exit
			fi
				echo "`egrep ^$user: /etc/passwd`"|awk 'BEGIN{
				FS=":"}
				{
			        printf "Usuario: "$1"\nIdentificador de usuario: "$3"\nIdentificador de grupo: "$4"\nGECOS: "$5"\nHOME: "$6"\nSHELL: "$7"\n\n"
				print "*********************************************"}'
                elif [ "$3" = "-C" ]
                then
			. ./CamPass.sh
                else
                        echo Argmento no valido
                fi
	elif [ "$2" = "-GP" -a "$#" -eq "2" ]
	then
		echo "`logname` ingreso a gestion de procesos el `date +"%D a las %H:%M:%S"`">>./bitacora.log
		ps ax | tr -s [:blank:]  |awk '
                                        {
                                        printf "Identificador: "$1"\tNombre del Proceso: "$5"\n"
                                        print "*********************************************"}'
			echo "Quieres enviar una senal a algun proceso?[s/n]"
			read op
			if [ "$op" = "s" ]
			then
				echo "19.-SigStop"
				echo "18.-SigCont"
				echo "15.-SigTerm"
				echo "9.-SigKill"
				echo "Que senal deceas enviar?"
				read senal
				if [ `echo "$senal" | egrep -v '^(19|18|15|9)$'` ]
				then
					echo No existe esa opcion
					exit
				fi
				echo "Ingresa el identificador del proceso al que deceas enviar esa senal: "
                                read pros
                                if [ "`ps ax | cut -d" " -f1 | egrep -v $pros`" = "" ]
				then
                                        echo No existe ese proceso
                                        exit
				fi
				kill -$senal $pros
				echo Se envio la senal correctamente
			else 
				echo "Adios :)"
				exit
			fi
	elif [ "$2" = "-R" -a "$#" -eq "3" ]
	then
		if [ "$3" = "-C" ]
                then
			echo "`logname` hizo un empaquetado completo el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			echo Que archivo deceas empaquetar?
			read archi
			test -r $archi
	                if [ "$?" -ne "0" ]
        	        then
                	        echo Ese archivo no existe
				exit
        	        fi
        	        echo Ingresa el nuevo nombre del empaquetado
                        read emp
			echo Empaquetando:
               	        tar -cvzf  $emp $archi  2>>errores.log
                elif [ "$3" = "-I" ]
                then
			echo "`logname` hizo un empaquetado incremental el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			echo Que archivo deceas empaquetar?
                        read archi
			test -r $archi
     		        if [ "$?" -ne "0" ]
			then
                            echo Ese archivo no tiene permisos de lectura
			    exit
                        fi
                            echo Ingresa el nuevo nombre del empaquetado
                            read emp
                            rsync -vax --progress  $archi $emp  2>>errores.log
                elif [ "$3" = "-D" ]
                then
			echo "`logname` hizo un empaquetado diferencial el `date +"%D a las %H:%M:%S"`">>./bitacora.log
			echo Que archivo deceas empaquetar?
                        read archi
                        if [ "$?" -ne "0" ]
			then
				echo Ese archivo no tiene permiso de lectura
				exit
                        fi
                              echo Ingresa el nuevo nombre del empaquetado
			      read emp
                              rsync -vax --progress  $archi $emp  2>>errores.log
   		 else
                         echo Argmento no valido
                 fi

	else 
		echo Argumento no valido
		exit

	fi	
elif [ "$1" = "-OB" -a "$#" -eq "2" ]
then
	if [ "$2" = "-m" ]
        then
	#mv
		echo "`logname` hizo un mv el `date +"%D a las %H:%M:%S"`">>./bitacora.log
		echo Ingresa el nombre del archivo a renombrar
		read nomv
		test -r $nomv
		if [ "$?" -ne "0" ]
		then
			echo Ese archivo no existe
		        exit
		fi		
		echo Ingresa el nuevo nombre
		read nomn
		mv $nomv $nomn 2>errores.log
        elif [ "$2" = "-c" ]
        then
		echo "`logname` ingreso a cp el `date +"%D a las %H:%M:%S"`">>./bitacora.log
		echo Ingresa el nombre del archivo a copiar
                read cop
                nu=0
		if [ -r $cop ]
		then
	                test -r $cop
			if [ "$?" -ne 0 ]
			then
                	       echo Ese archivo no existe
	                       exit
        	        fi
                	echo Ingresa el nombre de la copia
	                read ncop
        	       	cp -r $cop $ncop 2>>errores.log
		else
			echo No tiene permiso de escritura
			exit
		fi
        elif [ "$2" = "-f" ]
        then
		#find
		echo "`logname` ingreso a find el `date +"%D a las %H:%M:%S"`">>./bitacora.log
		echo Ingresa el nombre del archivo a buscar
		read bus
		echo Ingresa en donde queires buscar	
		read lugar
		clear
		echo Resultado de busqueda: 
		find $lugar -name $bus 2>>errores.log
        elif [ "$2" = "-mk" ]
        then
		#mkdir
		echo "`logname` ingreso a mkdir el `date +"%D a las %H:%M:%S"`">>./bitacora.log
		echo Ingresa el nombre del directorio que deceas crear
		read dire
		mkdir -p $dire
	elif [ "$2" = "-cr" ]
	then
		#crone
		#	min, horas, diames, mes, diasemana
		echo "`logname` ingreso a cron el `date +"%D a las %H:%M:%S"`">>./bitacora.log
		echo "Ingresa cada cuanto tiempo quieres que se repita (minutos horas diadelmes mes diasemana)"
                read tiempo
		 if [ "$(echo "$tiempo" | egrep '(^(([0-5]*[0-9])((-|,)[0-5]*[0-9])*|\*) (([0-1]*[0-9]|2[0-4])((-|,)[0-1]*[0-9]|-2[0-4])*|\*) (([1-9]|[12][0-9]|3[01])((-|,)[1-9]|[12][0-9]|-3[01])*|\*) (([1-9]|1[0-2])((-|,)[1-9]|-1[0-2])*|\*) ((([0-6])((-|,)[0-6])*)|\*)$)|^\*/[0-9]+ \*/[0-9]+ \*/[0-9]+ \*/[0-9]+ \*/[0-9]+$)')" ]
                then
                     	echo Ingresa el comando a ejecutar
                     	read comand
                	echo "$tiempo" "$comand" | crontab
		else
			echo Argumentos no validos
			exit
		fi
        else
            echo Argmento no valido
        fi

elif [ "$1" = "-OSA" -a "$#" -eq "2" ]
then
        if [ "$2" = "-AD" ]
        then
		echo "`logname` ingreso a ver archivos repetidos el `date +"%D a las %H:%M:%S"`">>./bitacora.log
		#archivos repetidos
		echo "Ingresa la ruta del directorio que deceas ver si tiene archivos con contenido repetido"
		read ruta
		test -d $ruta
		if [ $? -eq 0 ]
		then
			>temp
			gu=IFS
			IFS=$'\n'
			for var in `find $ruta`
			do
				test -d $var
				if [ $? -ne 0 ]
				then
       					sha512sum $var >>temp
				fi
			done
			IFS=$gu
			for nor in `sort temp | cut -d' ' -f1 | uniq -u`
			do
        			sed '/'$nor'/d' ./temp>temp2
       				cat temp2 > temp
			done
			if [ "`cat temp`" != '' ]
			then
				echo Los siguientes archivos son iguales en contenido
				for rep in `cut -d' ' -f1 temp | sort -u`
				do
        				egrep $rep temp | cut -d' ' -f3
        				echo '***********************************************'
				done
			else 
				echo "No hay archivos repetidos"
			fi
		else 
			echo No es un directorio
		fi	
	elif [ "$2" = "-C" ]
	then
		echo "`logname` ingreso a cifrar el `date +"%D a las %H:%M:%S"`">>./bitacora.log
		echo 'Ingresa el nombre del archivo que deceas cifrar'
		read ar
		clear
		test -r $ar
		if [ "$?" -ne 0 ]
		then 
			echo No existe ese archivo o no tiene permiso de lectura, ingresa otro por favor
			exit
		fi	
		if [ -d $ar ]
                then
                        echo Es un directorio
			exit
                fi
		if [ -r $ar.gpg ]
		then
                        echo Ya existe ese archivo cifrado
                        exit
		fi
		echo "Ingresa una contrasena segura (13 caracteres, al menos un numero, una letra minuscula, una mayuscula, y dos simbolos (#$%&.))"
		stty -echo
		read contra
		clear
		if [ "$(echo $contra|wc -m)" -ge "13" -a "$(echo $contra|egrep '[0-9]')" -a "$(echo $contra|egrep '[a-z]')" -a "$(echo $contra|egrep '[A-Z]')" -a "$(echo $contra|egrep '[#$%&.]')" ]
		then
        		if [ "$(echo $contra | egrep -o . | egrep -v '([0-9]|[a-z]|[A-Z]|[#$%&.])')" ]
        		then
               			echo Contrasena no valida
				exit
			else
				if [ "$(echo $contra | wc -c)" -ge "13" ]
				then
					echo "Ingresa nuevamente la contrasena"
					stty -echo
					read contra2
					stty echo
					if [ "$contra" = "$contra2" ]
					then
						echo $contra| gpg --batch -c --passphrase-fd 0 $ar 2>>errores.log
					else
						echo Las contrasenas no coinciden
						exit
					fi
				fi
			fi
		else
			echo Contrasena no valida
			exit
		fi
				echo ""
        else
            echo Argmento no valido
        fi

elif [ "$1" = "-IG" -a "$#" -eq "2" ]
then
	if [ "$2" = "-UC" ]
        then
		echo "`logname` ingreso a ver los usuarios conectados el `date +"%D a las %H:%M:%S"`">>./bitacora.log
		#usuariosconectados
		for var in $(w -h | cut -d' ' -f1)
                do
			echo "Usuario: $var"
			echo "Terminal: $(w -h $var | tr -s [:blank:] | tr -d : | cut -d' ' -f2)"
			echo "Nodo remoto: $(w -h $var | tr -s [:blank:] | tr -d : | cut -d' ' -f3)"
			echo "Tiempo de conexion:  $(w -h $var | tr -s [:blank:] | cut -d' ' -f4)"  
			echo "Tiempo inactivo: $(w -h $var | tr -s [:blank:] | cut -d' ' -f5)"
			echo "JCPU: $(w -h $var | tr -s [:blank:] | cut -d' ' -f6)"
			echo "PCPU: $(w -h $var | tr -s [:blank:] | cut -d' ' -f7)"
	        done
        elif [ "$2" = "-T" ]
        then
		echo "`logname` ingreso a ver el tiempo que lleva arriba la maquina el `date +"%D a las %H:%M:%S"`">>./bitacora.log
		echo Tiempo arriba: $(uptime | tr ',' / | cut -d/ -f1 | egrep -o 'up .*' |tr -d 'up ')  2>>errores.log
        else
        	echo Argmento no valido
        fi
else 
	echo Argumento no valido
	exit

fi
