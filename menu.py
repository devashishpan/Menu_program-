import os,getpass
import Dockermenu.dockermenu as dm
import Hadoopmenu.hadoop_menu as hm
import AWSmenu.aws_menu as am
import LVMmenu.lvm_menu as lm
import subprocess as sp

def check_pass():
	passwd=int(getpass.getpass('Enter sudo password : '))
	data=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S date')
	if 'incorrect password' in data:
		input('Incorrect password....press enter.....')
		return 12

def set_server():
	passwd=int(getpass.getpass('Enter sudo password : '))
	if 'httpd.service could not be found.' in sp.getoutput('systemctl status httpd'):
		c=input('Installing Webserver...(y/N) :')
		if c=='y':
			os.system(f'echo \'{passwd}\n\'| sudo -S yum install httpd')
		else :
			print('Web server program could not be isntalled....\n')
			return
	else:
		os.system(f'echo \'{passwd}\n\'| sudo -Ssystemctl enable httpd')
		os.system(f'echo \'{passwd}\n\'| sudo -Ssystemctl start httpd')

def dis_se():
	passwd=int(getpass.getpass('Enter sudo password : '))
	os.system(f'echo \'{passwd}\n\'| sudo -S setenforce 0')

def ena_se():
	passwd=int(getpass.getpass('Enter sudo password : '))
	os.system(f'echo \'{passwd}\n\'| sudo -S setenforce 1')

def dis_firewall():
	passwd=int(getpass.getpass('Enter sudo password : '))
	os.system(f'echo \'{passwd}\n\'| sudo -S systemctl stop firewalld')
	os.system(f'echo \'{passwd}\n\'| sudo -S systemctl disable firewalld')

def create_user():
	passwd=int(getpass.getpass('Enter sudo password : '))
	name=input('Enter user name : ')
	os.system(f'echo \'{passwd}\n\'| sudo -S useradd {name}')
	os.system(f'echo \'{passwd}\n\'| sudo -S passwd {name}')

def date():
	os.system('date')

def pwd():
	os.system('pwd')

menu_='''\t\t1. AWS MENU
\t\t2. DOCKER MENU
\t\t3. HADOOP MENU
\t\t4. LVM MENU
\t\t5. Date
\t\t6. Present Working Directory
\t\t7. Create User
\t\t8. Stop firewalld
\t\t9. Enable SELinux
\t\t10 Disable SELinux
\t\t11. Set up Web Server
\t\t12. EXIT
'''
def menu():
	choice=0
	choice = check_pass()
	while(choice!=12):
		os.system('clear')
		print('\t\t\t\tWelcome To LINUX Menu!\n\n')
		print(menu_)
		choice=int(input('\n\tEnter Your Choice : '))
		if choice == 1:
			print('-----------------------------------------------------------\n')
			am.aws_menu()
			input('\nPress enter to continue...')
		elif choice == 2:
			print('-----------------------------------------------------------\n')
			dm.docker_menu()
			input('\nPress enter to continue...')
		elif choice == 3:
			print('-----------------------------------------------------------\n')
			hm.hadoop_menu()
			input('\n\nPress enter to continue...')
		elif choice == 4:
			print('-----------------------------------------------------------\n')
			lm.lvm_menu()
			input('\nPress enter to continue...')
		elif choice == 5:
			print('-----------------------------------------------------------\n')
			date()
			input('\nPress enter to continue...')
		elif choice == 6:
			print('-----------------------------------------------------------\n')
			pwd()
			input('\nPress enter to continue...')
		elif choice == 7:
			print('-----------------------------------------------------------\n')
			create_user()
			input('\nPress enter to continue...')
		elif choice == 8:
			print('-----------------------------------------------------------\n')
			dis_firewall()
			input('\nPress enter to continue...')
		elif choice == 9:
			print('-----------------------------------------------------------\n')
			ena_se()
			input('\nPress enter to continue...')
		elif choice == 10:
			print('-----------------------------------------------------------\n')
			dis_se()
			input('\nPress enter to continue...')
		elif choice == 11:
			print('-----------------------------------------------------------\n')
			set_server()
			input('\nPress enter to continue...')
		elif choice == 12:
			s=input('Are you sure you want to leave LINUX MENU....(y/N) : ')
			if s=='y':
				choice=12
			else:
				choice=0
menu()

