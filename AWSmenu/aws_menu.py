#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,subprocess
import AWSmenu.launch_instance as li
import AWSmenu.create_key as ck
import AWSmenu.create_sg as cs

def check_for_int():
	print('Checking for internet access.......')
	c=subprocess.getoutput('curl -I https://www.google.com')
	if 'HTTP/1.1 200 OK' not in c :
		input('Connect to a network with internet connection and try again......\n\n\tPress any key to continue.....')
		return 7
	else:
		return 0
menu='''\n\t\t1 : Launch an ec2 instance from saved configuration.
\t\t2 : Launch an ec2 instance.
\t\t3 : Launch instance from a new Image.
\t\t4 : Create a Key-Pair
\t\t5 : List the instances.
\t\t6 : Create a security group.
\t\t7 : EXIT
'''
def aws_menu():
	choice=0
	choice = check_for_int()
	while(choice!=7):
		os.system('clear')
		print('\t\t\t\tWelcome To AWS Menu!')
		print(menu)
		choice=int(input('\n\tEnter Your Choice : '))
		if choice == 1:
			print('-----------------------------------------------------------\n')
			count=int(input('Enter the number of instances to be launched : '))
			li.launch_from_con(count)
			input('\nInstance lauched...Press enter to continue...')
		elif choice == 2:
			print('-----------------------------------------------------------\n')
			count=int(input('Enter the number of instances to be launched : '))
			li.launch_instance(count)
			input('\nInstance lauched...Press enter to continue...')
		elif choice == 3:
			print('-----------------------------------------------------------\n')
			count=int(input('Enter the number of instances to be launched : '))
			li.launch_from_image(count)
			input('\nInstance lauched...\nPress enter to continue...')
		elif choice == 4:
			print('-----------------------------------------------------------\n')
			ck.create_key()
			input('\nKey Created.....Press enter to continue...')
		elif choice == 5:
			print('-----------------------------------------------------------\n')
			li.list_instances()
			input('\nPress enter to continue...')
		elif choice == 6:
			print('-----------------------------------------------------------\n')
			cs.create_sg()
			input('\nSecurity Group Created....Press enter to continue...')
		elif choice == 7:
			s=input('Are you sure you want to leave AWS MENU....(y/N) : ')
			if s=='y':
				choice=7
			else:
				choice=0
