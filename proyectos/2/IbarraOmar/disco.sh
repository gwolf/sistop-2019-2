#!/bin/bash
df -h | egrep "^/dev/sda" | tr -s [:blank:] '/' | awk 'BEGIN{
                                FS="/"
                                print "Particion | Espacio libre | Espacio total"}
                                {print $3"          "$6"              "$4}'
