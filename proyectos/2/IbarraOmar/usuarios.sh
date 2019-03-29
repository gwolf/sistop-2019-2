#!/bin/bash
for var in $(who | cut -d" " -f1 | sort -u)
                                do
                                        echo "Usuario: $var"
                                        echo "Sesiones: $(who | cut -d" " -f1 | grep -c $var)"
                                        echo "Procesos: $(expr  $(ps aux | grep ^$var | grep -v 'grep ^'$var'' | wc -l) - 1)"
                                        echo "Peso del directorio hogar :  $(sudo du -hs /home/$var |tr [:blank:] "/"| cut -d"/" -f1)"  
                                done
