#!/bin/bash
free -mo | tail -n +2 | tr -s [:blank:] ':'| awk 'BEGIN{
                                FS=":"
                                print "Tipo    | Espacio libre    | Espacio total"}
                                {printf $1"\t\t"$4"\t\t"$2"\n"}'
