#Autores: Carlos Gamaliel Morales Téllez y Miguel Ángel Pérez Quiroz
#Descripción: Micro sistema de archivos. 
import os
import subprocess
import time
from datetime import datetime

file_names = []
file_content_locator = []
file_sizes = []

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
	for i in range(0,64): #Aquí es 64 por que es el tamaño del directorio 1024 * 4 = 4096 = 64bytes*64
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
	


def get_existing_files(disk_name):
	''' 
	Por la forma en la que trabaja el sistema se debe obtener una lista con los 
	nombres de archivos. 
	'''
	file_system_disk = open(disk_name,'r')
	actual_pointer_aux = init_dir
	'''
	Debido a que los clusters para el directorio son 4 y cada uno mide 1024, 
	la longitud del directorio es 4096, pero al iniciar en 1024, el límite 
	queda en 5120 
	'''
	while actual_pointer_aux < 5120:
		file_system_disk.seek(actual_pointer_aux)
		query = file_system_disk.read(15)
		if query != 'AQUI_NO_VA_NADA':
			file_names.append(query.replace(" ",""))
			file_system_disk.seek(actual_pointer_aux+16)
			file_sizes.append(int(file_system_disk.read(8)))

			file_position = 0 
			for i in range(len(file_sizes)-1,0,-1):
				file_position += file_sizes[i] + 4

			file_position += 5120

			file_content_locator.append(file_position)

		actual_pointer_aux = actual_pointer_aux + 64

	actual_pointer_aux = 5120
	
	#while actual_pointer_aux < so.path.getsize(disk_name):
	#	file_system_disk.seek(actual_pointer_aux)


	#file_system_disk.close()



def insert_bytes(init_byte,limit_byte,word):

	if len(word) < (limit_byte-init_byte):
		try:
			int(word)
			for i in range((limit_byte-init_byte)-len(word)):
				word = '0' + word 
		except ValueError:
			for i in range((limit_byte-init_byte)-len(word)):
				word = ' ' + word
	try:	
		file_system_disk = open('FiUnamFS.img','r+')

	except FileNotFoundError: 
		file_system_disk = open('FiUnamFS.img','w') 

	file_system_disk.seek(init_byte)
	file_system_disk.write(word)			
	file_system_disk.close()


def copy_from_computer_to_disk(route,disk_name):
	global init_dir, file_content_locator
	actual_pointer_for_insert = init_dir
	computer_file = open(route,'r')
	file_system_disk = open(disk_name,'r+')
	file_name =  os.path.basename(route)
	sizeof_file =  str(os.path.getsize(route))
	init_cluster = str((actual_pointer_for_insert % 1024)+1)
	c_date = str(datetime.today().strftime('%Y%m%d%H%M%S')) #Fecha de creación (¿Se debe obtener del archivo?)
	m_date = str(datetime.today().strftime('%Y%m%d%H%M%S')) #Fecha de modificación (¿Se debe obtener del archivo?)
	file_content = computer_file.read()
	flag = 0
	while flag == 0:
		file_system_disk.seek(actual_pointer_for_insert)
		query = file_system_disk.read(15)
		if query == 'AQUI_NO_VA_NADA':
			file_names.append(file_name)
			file_sizes.append(os.path.getsize(route))

			insert_bytes(actual_pointer_for_insert,actual_pointer_for_insert+15,file_name)
			insert_bytes(actual_pointer_for_insert+16,actual_pointer_for_insert+24,sizeof_file)
			insert_bytes(actual_pointer_for_insert+25,actual_pointer_for_insert+30,init_cluster)
			insert_bytes(actual_pointer_for_insert+31,actual_pointer_for_insert+45,c_date)
			insert_bytes(actual_pointer_for_insert+46,actual_pointer_for_insert+60,m_date)

			file_content_locator.append(os.path.getsize(disk_name)+4)
			insert_bytes(os.path.getsize(disk_name)+4,os.path.getsize(disk_name)+os.path.getsize(route),file_content)
			#Valida si no es el primero que sea mayor, si no, el archivo a insertar está vacío
			if len(file_content_locator) > 1:
				if file_content_locator[-1] == file_content_locator[-2]:
					file_content_locator[-1] = file_content_locator[-2] + 4

			
			flag = 1


		actual_pointer_for_insert = actual_pointer_for_insert + 64


	file_system_disk.close()
	computer_file.close()


def copy_from_disk_to_computer(file_name,disk_name):
	new_file = open(file_name,'w')
	file_system_disk = open(disk_name,'r')
	file_position = file_names.index(file_name)
	file_size = file_sizes[file_position]
	file_pointer = file_content_locator[file_position]
	file_system_disk.seek(file_pointer)
	new_file.write(file_system_disk.read(file_size))
	file_system_disk.close()
	new_file.close()

def list_files(disk_name):
	global file_names, file_sizes
	for file_name in file_names:
		index = file_names.index(file_name)
		print(file_name + '\t' + str(file_sizes[index]) + '\t')


def delete_file(file_name,disk_name):
	actual_pointer_for_delete = init_dir
	file_system_disk = open(disk_name,'r+')
	flag = 0
	while flag == 0: 
		file_system_disk.seek(actual_pointer_for_delete)
		query = file_system_disk.read(15)
		if query.replace(" ","") == file_name:
			insert_bytes(actual_pointer_for_delete,actual_pointer_for_delete+15,'AQUI_NO_VA_NADA')
			insert_bytes(actual_pointer_for_delete+16,actual_pointer_for_delete+24,'00000000')
			insert_bytes(actual_pointer_for_delete+25,actual_pointer_for_delete+30,'00000000')
			insert_bytes(actual_pointer_for_delete+31,actual_pointer_for_delete+45,'00000000000000')
			insert_bytes(actual_pointer_for_delete+46,actual_pointer_for_delete+60,'00000000000000')
			index = file_names.index(file_name)
			location = file_content_locator[index]
			for i in range(file_sizes[index] + 4):
				file_system_disk.seek(location)
				file_system_disk.write('0')
				location += 1

			
			file_names.remove(file_name)
			del file_sizes[index]
			del file_content_locator[index]

			flag = 1

		actual_pointer_for_delete = actual_pointer_for_delete + 64
	
	file_system_disk.close()

def disk_defragmenter(disk_name):
	pass


def user_interface(disk_name):
	try: 
		file_system_disk = open(disk_name,'r+')
		file_system_disk.close()
		get_existing_files(disk_name)

	except FileNotFoundError: 
		create_file_system_disk()

	while True:
		print('-----------------Gracias por usar FiUnamFS----------------')
		print('Si eres nuevo utilizando FiUnamFS puedes utilizar el ')
		print('comando help para obtener ayuda.\n')
		option = input('FiUnamFS# ')
		command = option[:option.find(" ")]
		if option == 'exit' or command == 'exit':
			break
		elif command == 'copyfc':
			file_name = option[option.find(" ")+1:]
			copy_from_computer_to_disk(file_name,disk_name)
			#print(file_names)
			#print(file_sizes)
			#print(file_content_locator)
		elif command == 'copyfs':
			file_name = option[option.find(" ")+1:]
			copy_from_disk_to_computer(file_name,disk_name)	
			#print(file_names)
			#print(file_sizes)
			#print(file_content_locator)
		elif command == 'delete':
			file_name = option[option.find(" ")+1:]
			delete_file(file_name,disk_name)
			#print(file_names)
			#print(file_sizes)
			#print(file_content_locator)
		elif command == 'list' or option == 'list':
			list_files(disk_name)


	
user_interface(disk_name)




