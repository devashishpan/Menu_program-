#-----imports------------------------
import subprocess as sp
import getpass
#-----imports------------------------


#-----------------Physical Volumes-------------------------------
def create_pv(storage_device_name):
	passwd=int(getpass.getpass('Enter sudo password : '))
	dump=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S pvcreate {storage_device_name}')
	print(dump)

def remove_pv(physical_vol_path):
	passwd=int(getpass.getpass('Enter sudo password : '))
	dump=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S pvremove {physical_vol_path}')
	print(dump)
#-----------------Physical Volumes-------------------------------


#----------------Volume Group------------------------------------
def create_vg(vol_group_name,physical_vol_path):
	passwd=int(getpass.getpass('Enter sudo password : '))
	dump=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S vgcreate {vol_group_name} {physical_vol_path}')
	print(dump)

def extend_vg(vol_group_name,physical_vol_path):
	passwd=int(getpass.getpass('Enter sudo password : '))
	dump=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S vgextend {vol_group_name} {physical_vol_path}')
	print(dump)

def reduce_vg(vol_group_name,logical_vol_path):
	passwd=int(getpass.getpass('Enter sudo password : '))
	dump=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S vgreduce {vol_group_name} {logical_vol_path}')
	print(dump)

def remove_vg(volume_group_path):
	passwd=int(getpass.getpass('Enter sudo password : '))
	dump=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S vgremove {volume_group_path}')
	print(dump)
#----------------Volume Group------------------------------------


#----------------Logical Volumes---------------------------------
def create_lv(logical_vol_name,vol_group_name):
	passwd=int(getpass.getpass('Enter sudo password : '))
	dump=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S lvcreate --name {logical_vol_name} /dev/{vol_group_name}')
	print(dump)

def extend_lv(logical_vol_name,vg,size):
	passwd=int(getpass.getpass('Enter sudo password : '))
	dump=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S lvextend --size +{size} /dev/{vg}/{logical_vol_name}')
	print(dump)
	dump=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S resize2fs /dev/{vg}/{logical_vol_name}')
	print(dump)

def reduce_lv(logical_vol_path,size):
	passwd=int(getpass.getpass('Enter sudo password : '))
	dump=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S lvreduce -L --size -{size} {logical_vol_path}')
	print(dump)
	dump=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S resize2fs {logical_vol_path}')
	print(dump)

def remove_lv(logical_vol_path):
	passwd=int(getpass.getpass('Enter sudo password : '))
	dump=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S lvremove {logical_vol_path}')
	print(dump)
#----------------Logical Volumes---------------------------------


#---------------Listings-----------------------------------------
def list_pd():
	dump=sp.getoutput('lsblk -all | grep disk')
	dump=dump.split('\n')
	return dump

def list_pp():
	dump=sp.getoutput('lsblk -all | grep part')
	dump=dump.split('\n')
	return dump

def list_plvm():
	dump=sp.getoutput('lsblk -all | grep lvm')
	dump=dump.split('\n')
	return dump

def list_pv():
	passwd=int(getpass.getpass('Enter sudo password : '))
	dump=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S pvs')
	return dump

def list_vg():
	passwd=int(getpass.getpass('Enter sudo password : '))
	dump=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S vgs')
	return dump

def list_lv():
	passwd=int(getpass.getpass('Enter sudo password : '))
	dump=sp.getoutput(f'echo \'{passwd}\n\'| sudo -S lvs -o +devices')
	return dump
#---------------Listings-----------------------------------------


