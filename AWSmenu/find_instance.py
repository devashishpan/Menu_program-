#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os,json
import subprocess as sp

def find_ins_type():
    os.system('clear')
    pwd=sp.getoutput('pwd')
    d=sp.getstatusoutput(f'find {pwd}/AWS/instance_type.json')
    if d[0]!=0:
        with open(f'{pwd}/AWS/instance_type_detailed.json','w') as fw:
            data=sp.getoutput("aws ec2 describe-instance-types")
            fw.write(data)
    del d
    choice=0
    with open(f'{pwd}/AWS/files/instance_type.json','r') as fr:
        data=json.load(fr)
        del fr
    while(choice!=-1):
        os.system('clear')
        print('Listing all Instance-types on this System .....\n')
        for i in data["InstanceTypes"]:
            print(f'\t{i["Sr. No."]} . {i["Name"]} : {i["Description"]}')
        j=i["Sr. No."]
        try:
            choice=int(input('Enter the serial number of the desired instance type: '))
        except:
            print('Enter a valid choice...')
        if choice<=0 | choice>j:
            print('Enter a valid choice......')
            choice=0
            input('Press enter to continue...')
            os.system('clear')
        else:
            print('Your choice : ')
            for i in data["InstanceTypes"]:
                if int(i["Sr. No."])==choice:
                    print(f'\t{i["Sr. No."]}.{i["Name"]} : {i["Description"]}')
                    print('Detailed Description:::---------------------------------')
                    os.system(f'aws ec2 describe-instance-types --instance-type {i["Name"]}')
                    con=input('\nConfirm Your Choice(y/n):')
                    if con=='y':
                        choice=-1
                        sch=i["Name"]
                        del data,j,i
                    else:
                        choice=0
                    break
    del choice,pwd
    os.system('clear')
    return sch

def add_instance():
    os.system('clear')
    pwd=sp.getoutput('pwd')
    with open(f'{pwd}/AWS/files/instance_type.json','r') as fr:
        data=json.load(fr)
        sr_no=1+data["InstanceTypes"][-1]["Sr. No."]
        des=input('Enter the Instance Description : ')
        name=input('Enter the instance name : ')
        new_entry={"Description" : des,
            		"Name" : name,
                    "Sr. No." : sr_no
                    }
        if new_entry in data["InstanceTypes"]:
            print('Entry already in file......')
            os.system('clear')
            del pwd,data,fr,des,sr_no
            return name
        else:
            data["InstanceTypes"].append(new_entry)
            fr.write(data)
        fr.close()
    del pwd,data,fr,des,sr_no
    os.system('clear')
    return name