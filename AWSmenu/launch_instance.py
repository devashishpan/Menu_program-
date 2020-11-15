#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,json,time
import subprocess as sp
import AWSmenu.find_ami as fa
import AWSmenu.find_instance as fi
import AWSmenu.create_key as ck
import AWSmenu.create_sg as cs

def launch_instance(count):
    os.system('clear')
    image_id=fa.find_ami()
    instance_type=fi.find_ins_type()
    MyKeyPair=ck.find_key()
    sg_id=cs.find_sg()
    print('Instance Details:.......')
    print(f'Ami Name = {image_id[1]}\nINstance Type = {instance_type}\n Number of instances = {count}\nKey-Pair ID = {MyKeyPair}\nSecurity Group = {sg_id[1]}')
    c=input('Do You Wish To Continue.....(y/n) : ')
    if c=='y':
        os.system(f'aws ec2 run-instances --image-id {image_id[0]} --count {count} --instance-type {instance_type}--key-name {MyKeyPair} --security-group-ids {sg_id[0]}')
        print('\n\nInstance Launched......Wait for 10 seconds......')
        time.sleep(10)
        list_instance_file()
        print('Launched Instances File Updated.........')
        launch_inctance_con_file(image_id,instance_type,MyKeyPair,sg_id)
        print('Launched Instances Configuration File Updated.........')
    else:
        pass
def launch_from_image(count):
    os.system('clear')
    instance_type=fi.add_instance()
    image_id=fa.add_ami()
    MyKeyPair=ck.find_key()
    sg_id=cs.find_sg()
    print('Instance Details:.......')
    print(f'Ami Name = {image_id[1]}\nINstance Type = {instance_type}\n Number of instances = {count}\nKey-Pair ID = {MyKeyPair}\nSecurity Group = {sg_id[1]}')
    c=input('Do You Wish To Continue.....(y/n) : ')
    if c=='y':
        os.system(f'aws ec2 run-instances --image-id {image_id[0]} --count {count} --instance-type {instance_type}--key-name {MyKeyPair} --security-group-ids {sg_id[0]}')
        print('\n\nInstance Launched......Wait for 10 seconds......')
        time.sleep(10)
        list_instance_file()
        print('Launched Instances File Updated.........')
        launch_inctance_con_file(image_id,instance_type,MyKeyPair,sg_id)
        print('Launched Instances Configuration File Updated.........')
    else:
        pass

def launch_from_con(count):
    pwd=sp.getoutput('pwd')
    print('Launching Instance from  Configuration File.........')
    with open(f'{pwd}/AWS/files/Launched_instance_con_details.json','r') as fr:
        data=json.load(fr)
    choice=0
    while(choice!=-1):
        os.system('clear')
        print('List of Configurations on the system....')
        for i in data["InstancesCon"]:
            print(f'\t{i["LaunchIndex"]} . {i["ImageId"]} : {i["SGId"]} : {i["InstanceType"]}: {i["KeyName"]}')
        j=i["LaunchIndex"]
        try:
            choice=int(input('Enter the serial number of the desired Configuration : '))
        except:
            print('Enter a val(id choice...')
        if choice<=0 | choice>int(j):
            print('Enter a valid choice......')
        else:
            i=data["InstancesCon"][choice-1]
            print(f'\t{i["LaunchIndex"]} . {i["ImageId"]} : {i["SGId"]} : {i["InstanceType"]}: {i["KeyName"]}')
            con=input('\nConfirm Your Choice(y/n):')
            if con=='y':
                os.system(f'aws ec2 run-instances --image-id {i["ImageId"][0]} --count {count} --instance-type {i["InstanceType"]}--key-name {"KeyName"} --security-group-ids {i["SGId"][0]}')
                print('\n\nInstance Launched......Wait for 10 seconds......')
                time.sleep(10)
                list_instance_file()
                print('Launched Instances File Updated.........')
                choice=-1
                del i,j,data,pwd,con
            else:
                choice=0

def list_instance_file():
    pwd=sp.getoutput('pwd')
    print('Updating Launched Instances File.........')
    with open(f'{pwd}/AWS/files/Launched_instance_details.json','w') as fw:
        data=sp.getoutput('aws ec2 describe-instances')
        fw.write(data)
        fw.close()
    del pwd,data,fw

def list_instances():
    pwd=sp.getoutput('pwd')
    choice=0
    while(choice!=1):
        try:
            with open(f'{pwd}/AWS/files/Launched_instance_details.json','r') as fr:
                data=json.load(fr)
                del fr
                print('List of Instances in AWS Ec2 account......')
                for i in data["Reservations"][0]["Instances"]:
                	print(f'\t{1+i["AmiLaunchIndex"]}. {i["Tags"][0]["Value"]} : {i["InstanceId"]} : {i["State"]["Name"]}')
            del data,pwd
            choice=1
        except :
            list_instance_file()

def launch_inctance_con_file(image_id,instance_type,MyKeyPair,sg_id):
    pwd=sp.getoutput('pwd')
    print('Updating Launched Instances Configuration File.........')
    with open(f'{pwd}/AWS/files/Launched_instance_con_details.json','w+') as fw:
        data=json.load(fw)
        n=data["InstancesCon"][-1]["LaunchIndex"]
        new_entry={
				"LaunchIndex": n+1,
				"ImageId": image_id,
				"SGId": sg_id,
				"InstanceType": instance_type,
				"KeyName": MyKeyPair
			}
        if new_entry in data["InstancesCon"]:
            print('Entry already in file......')
            del pwd,data,fw
            return 0
        else:
            data["InstancesCon"].append(new_entry)
            fw.write(data)
        fw.close()
    del pwd,data,fw
