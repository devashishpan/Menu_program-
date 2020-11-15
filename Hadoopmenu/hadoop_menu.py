# -*- coding: utf-8 -*-
import os,getpass
import subprocess as sp

def check_for_hadoop():
	passwd=int(getpass.getpass('Enter sudo password : '))
	data=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S hadoop -version')
	if 'incorrect password' in data:
		return 6
	if 'java version "1.8.0_171"' in data:
		pass
	else:
		c=input('No hadoop software detected....Do You want to install Hadoop...(y/n) :')
		if c=='y':
			os.system('echo \'{passwd}\n\'| sudo yum install initscripts*')
			os.system('echo \'{passwd}\n\'| sudo rpm -i jdk-8u171-linux-x64.rpm --force')
			os.system('echo \'{passwd}\n\'| sudo rpm -i install hadoop-1.2.1-1.x86_64.rpm --force')
		else:
			return 6

def hadoop_nn_con():
	pwd=sp.getoutput('pwd')
	print()
	os.system('mkdir /nn')
	os.system('rm /etc/hadoop/hdfs-site.xml')
	os.system('rm /etc/hadoop/core-site.xml')
	os.system(f'cp -t  /etc/hadoop {pwd}/master/hdfs-site.xml')
	os.system(f'cp -t  /etc/hadoop {pwd}/master/core-site.xml')
	os.system('hadoop namenode -format')

def hadoop_cl_con():
	os.system('rm /etc/hadoop/core-site.xml')
	ip=input('Enter IP address of the master node : ')
	data=f'''<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{ip}:9001</value>
</property>
</configuration>'''
	with open('core-site.xml','w') as fw :
		fw.write(data)
	os.system('mv core-site.xml /etc/hadoop')

def hadoop_dn_con():
	pwd=sp.getoutput('pwd')
	os.system('mkdir /dn')
	os.system('rm /etc/hadoop/hdfs-site.xml')
	os.system('rm /etc/hadoop/core-site.xml')
	os.system(f'cp -t  /etc/hadoop {pwd}/slave/hdfs-site.xml')
	ip=input('Enter IP address of the master node : ')
	data=f'''<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{ip}:9001</value>
</property>
</configuration>'''
	with open('core-site.xml','w') as fw :
		fw.write(data)
	os.system('mv core-site.xml /etc/hadoop')

def hadoop_nn_start():
	os.system('hadoop-daemon start namenode')
	if 'NameNode' in sp.getoutput('jps'):
		pass
	else:
		input('Some Error Occured in Starting Master....press enter to continue....')

def hadoop_dn_start():
	os.system('hadoop-daemon start datanode')
	if 'DataNode' in sp.getoutput('jps'):
		pass
	else:
		input('Some Error Occured in Starting Slave....press enter to continue....')

def hadoop_menu():
	choice=0
	choice = check_for_hadoop()
	while(choice!=6):
		os.system('clear')
		print('\n\n\t\t\tHADOOP MENU\n')
		print('\t\t1. Configure Masternode \n\t\t2. Configure Slavenode\n\t\t3. Configure Client node\n\t\t4. Start Masternode\n\t\t5.Start Slavenode\n\t\t6. EXIT')
		choice=int(input('\n\tEnter Your Choice : '))
		if choice == 1:
			print('-----------------------------------------------------------\n')
			hadoop_nn_con()
			input('Masternode configured...\nPress enter to continue...')
		elif choice == 2:
			print('-----------------------------------------------------------\n')
			hadoop_dn_con()
			input('Slavenode configured...\nPress enter to continue...')
		elif choice == 3:
			print('-----------------------------------------------------------\n')
			hadoop_cl_con()
			input('Clientnode configured...\nPress enter to continue...')
		elif choice == 4:
			print('-----------------------------------------------------------\n')
			hadoop_nn_start()
			input('Masternode started...\nPress enter to continue...')
		elif choice == 5:
			print('-----------------------------------------------------------\n')
			hadoop_dn_start()
			input('Slavenode started...\nPress enter to continue...')
		elif choice == 6:
			s=input('Are you sure you want to leave HADOOP MENU....(y/N) : ')
			if s=='y':
				choice=5
			else:
				choice=0

