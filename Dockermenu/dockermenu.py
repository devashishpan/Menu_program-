#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os,getpass
import subprocess as sp

def check_for_docker():
	passwd=int(getpass.getpass('Enter sudo password : '))
	data=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S docker version')
	if 'incorrect password' in data:
		return 7
	if'command not found' in data :
		c=input('Do You want to install Docker...(y/n) :')
		if c=='y':
			os.system('echo \'{passwd}\n\'| sudo yum install -y yum-utils')
			os.system('echo \'{passwd}\n\'| sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo')
			os.system('echo \'{passwd}\n\'| sudo yum install docker-ce docker-ce-cli containerd.io')
		else :
			return 7
	else:
		pass

def pull_image():
	passwd=int(getpass.getpass('Enter sudo password : '))
	image=input('Enter OS name : ')
	os.system(f'echo \'{passwd}\n\'| sudo -S docker pull {image}')

def launch_con():
	passwd=int(getpass.getpass('Enter sudo password : '))
	name=input('Enter container name : ')
	list_image()
	os_name=input('Enter the OS name : ')
	os.system(f'echo \'{passwd}\n\'| sudo -S docker run --name {name} {os_name}')

def list_image():
	passwd=int(getpass.getpass('Enter sudo password : '))
	os.system(f'echo \'{passwd}\n\'| sudo -S docker images')

def list_con():
	passwd=int(getpass.getpass('Enter sudo password : '))
	os.system(f'echo \'{passwd}\n\'| sudo -S docker ps -a')

def rev_con():
	passwd=int(getpass.getpass('Enter sudo password : '))
	list_con()
	con_name=input('Enter Container name or ID : ')
	os.system(f'echo \'{passwd}\n\'| sudo -S docker rm {con_name}')

def rev_img():
	passwd=int(getpass.getpass('Enter sudo password : '))
	list_con()
	img_name=input('Enter Iamge name or ID : ')
	os.system(f'echo \'{passwd}\n\'| sudo -S docker rmi {img_name}')

def docker_menu():
	choice=0
	choice = check_for_docker()
	while(choice!=7):
		os.system('clear')
		print('\n\n\t\t\tDOCKER MENU\n')
		print('\t\t1. List images \n\t\t2. Pull image \n\t\t3. Launch container \n\t\t4. List containers\n\t\t5. Remove a Container \n\t\t6. Remove an image\n\t\t7. EXIT')
		choice=int(input('\n\tEnter Your Choice : '))
		if choice == 1:
			print('-----------------------------------------------------------\n')
			list_image()
			input('\nPress enter to continue...')
		elif choice == 2:
			print('-----------------------------------------------------------\n')
			pull_image()
			input('\nPress enter to continue...')
		elif choice == 3:
			print('-----------------------------------------------------------\n')
			launch_con()
			input('Container lauched...\nPress enter to continue...')
		elif choice == 4:
			print('-----------------------------------------------------------\n')
			list_con()
			input('\nPress enter to continue...')
		elif choice == 5:
			print('-----------------------------------------------------------\n')
			rev_con()
			input('\nContainer removed....Press enter to continue...')
		elif choice == 6:
			print('-----------------------------------------------------------\n')
			rev_img()
			input('\nImage removed....Press enter to continue...')
		elif choice == 7:
			s=input('Are you sure you want to leave DOCKER MENU....(y/N) : ')
			if s=='y':
				choice=7
			else:
				choice=0
