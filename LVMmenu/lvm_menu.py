import LVMmenu.lvm_methods as lm
import subprocess as sp
import os,getpass

def create_lvm():
	if input('Did You attach a new storage device (y/N) : ')=='y':
		print('List of Hard Disks : ')
		l=lm.list_pd()
		for i in range(len(l)):
			print(f'{i+1}. {l[i]}')
		print('E. Exit')
		print('Select the physical disk to be used : ',end ='')
		n=int(input())
		if n!=int('E'):
			l=l[n-1].split()
			lm.create_pv(f'/dev/{l[0]}')
			print(lm.list_pv())
			vg=input('Enter Volume Group name : ')
			lm.create_vg(vg,f'/dev/{l[0]}')
			print(lm.list_vg())
			lv=input('Enter Logical Volume name : ')
			lm.create_lv(lv,vg)
			print(lm.list_lv())
			print('Formating Created LVM partition....')
			print(sp.getoutput(f'mkfs.ext4 /dev/{vg}/{lv}'))
			folder=input('Enter the path for the directory to mount the lvm partition : ')
			if 'No such file or directory' in sp.getoutput(f'ls -l {folder}'):
				print(sp.getoutput(f'mkdir {folder}'))
			print(sp.getoutput(f'mount /dev/{vg}/{lv} {folder}'))
		else :
			print('Aborting Creation of new lvm partition.....')
	else :
		print('Aborting Creation of new lvm partition.....')

def extend_lvm():
	if input('Did You attach a new storage device (y/N) : ')=='y':
		print('List of Hard Disks : ')
		l=lm.list_pd()
		for i in range(len(l)):
			print(f'{i+1}. l[i]')
		print('E. Exit')
		print('Select the physical disk to be used : ',end ='')
		n=int(input())
		if n!=int('E'):
			l=l[n-1].split()
			lm.create_pv(f'/dev/{l[0]}')
			print('Listing Existing Volume groups.... ')
			print(lm.list_vg())
			vg=input('\nEnter Volume Group name : ')
			lm.extend_vg(vg,f'/dev/{l[0]}')
			print('Listing Existing Logical Volumes.... ')
			print(lm.list_lv())
			lv=input('\nEnter Logical Volume name : ')
			lm.extend_lv(lv,vg,input('Enter Space to be allocated to the logical volume : '))
		else :
			print('Aborting Creation of new lvm partition.....')
	else :
		print('Aborting Creation of new lvm partition.....')

def lvm_menu():
	choice=0
	passwd=int(getpass.getpass('Enter sudo password : '))
	data=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S apt list | grep lvm2-*')
	if 'incorrect password' in data:
		choice=3
		input('Incorrect password....press enter.....')
	if 'lvm2-' in data:
		pass
	else :
		c=input('Do You want to install LVM...(y/n) :')
		if c=='y':
			os.system('echo \'{passwd}\n\'| sudo yum install lvm2*')
		else:
			choice=3
	while(choice!=3):
		os.system('clear')
		print('\n\n\t\t\tLVM MENU\n')
		print('\t\t1. Create LVM Partition\n\t\t2. Extent LVM Partition\n\t\t3. EXIT')
		choice=int(input('\n\tEnter Your Choice : '))
		if choice == 1:
			print('-----------------------------------------------------------\n')
			#create_lvm()
			input('LVM Partition created...\nPress enter to continue...')
		elif choice == 2:
			print('-----------------------------------------------------------\n')
			#extend_lvm()
			input('LVM Partition extended...\nPress enter to continue...')
		elif choice == 3:
			s=input('Are you sure you want to leave LVM MENU....(y/N) : ')
			if s=='y':
				choice=3
			else:
				choice=0




