#!/bin/bash
uptime | egrep -o '[0-9]+\.[0-9]+'|tr -s '\n' ' ' | awk 'BEGIN{
                                                        printf "Carga del sistema\n"}
					{printf "Hace 5 minutos: "$1"\nHace 10 minutos: "$2"\nHace 15 minutos: "$3"\n"}'
