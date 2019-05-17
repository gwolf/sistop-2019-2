#Autores: Carlos Gamaliel Morales Téllez y Miguel Ángel Pérez Quiroz
#Descripción: Micro sistema de archivos. 
import os
import subprocess
import time
from datetime import datetime


file_system_name = 'FiUnamFS'
file_system_version = '0.4'
volume_tag = 'FiUnamFS.img' 
cluster_length = '1024'
num_of_clusters_dir = '4'
num_of_clusters_unit = '1440'

#El directorio inicia en el cluster 1 
init_dir = 1024
info_size = 64

disk_name = 'FiUnamFS.img'
actual_pointer = init_dir

def create_file_system_disk():
	global byte_number,file_system_name,file_system_version
	global volume_tag,cluster_length,num_of_clusters_dir,num_of_clusters_unit
	global actual_pointer
	insert_bytes(0,8,file_system_name)
	insert_bytes(10,13,file_system_version)
	insert_bytes(20,35,volume_tag)
	insert_bytes(40,45,cluster_length)
	insert_bytes(47,49,num_of_clusters_dir)
	insert_bytes(52,60,num_of_clusters_unit)
	for i in range(0,60):
		file_name = "AQUI_NO_VA_NADA"
		insert_bytes(0+actual_pointer,15+actual_pointer,file_name)
		size = '00000000'
		insert_bytes(16+actual_pointer,24+actual_pointer,size)
		init_cluster = '00000'
		insert_bytes(25+actual_pointer,30+actual_pointer,init_cluster)
		date = '00000000000000'
		insert_bytes(31+actual_pointer,45+actual_pointer,date)
		date_mod = '00000000000000'
		insert_bytes(46+actual_pointer,60+actual_pointer,date)

		#extra = '0000'
		#insert_bytes(61+actual_pointer,65+actual_pointer,extra)
		#El puntero iniciará en el byte 1024 
		actual_pointer = actual_pointer + 64


def insert_bytes(init_byte,limit_byte,word):

	if len(word) < (limit_byte-init_byte):
		try:
			int(word)
			for i in range((limit_byte-init_byte)-len(word)):
				word = '0' + word 
		except ValueError:
			for i in range((limit_byte-init_byte)-len(word)):
				word = ' ' + word
	file_system_disk = open('FiUnamFS.img','r+') 
	file_system_disk.seek(init_byte)
	file_system_disk.write(word)			
	file_system_disk.close()
