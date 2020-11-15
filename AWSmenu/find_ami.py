#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess as sp
import os
import json

def find_ami():
    os.system('clear')
    pwd=sp.getoutput('pwd')
    d=0
    while(d!=1):
        os.system('clear')
        os_type=input('Enter the OS type(Linux/Windows) : ')
        if (os_type =='Linux') | (os_type =='Windows'):
            d=1
    choice=0
    with open(f'{pwd}/AWS/files/ami-ids.json','r') as fr:
        data=json.load(fr)
        fr.close()
        del fr
    sch=''
    while(choice!=-1):
        print('List of Images on the system....')
        for i in data["Images"][0][f"{os_type}"]:
            print(f'\t{i["Sr. No."]} . {i["Name"]} : {i["ami-id"]}')
        j=i["Sr. No."]
        try:
            choice=int(input('Enter the serial number of the desired Image : '))
        except:
            print('Enter a val(id choice...')
        if choice<=0 | choice>int(j):
            print('Enter a valid choice......')
            input('Press enter to continue...')
            os.system('clear')
        else:
            print('Your choice : ')
            for i in data["Images"][0][f"{os_type}"]:
                if int(i["Sr. No."])==choice:
                    print(f'\t{i["Sr. No."]}.{i["Name"]} : {i["ami-id"]}')
                    con=input('Confirm Your Choice(y/n):')
                    if con=='y':
                        choice=-1
                        sch=[i["ami-id"],i["Name"]]
                        del data,j,i
                    else:
                        choice=0
                    break
    del choice,pwd
    return sch

def add_ami():
    os.system('clear')
    pwd=sp.getoutput('pwd')
    d=0
    while(d!=1):
        os.system('clear')
        os_type=input('Enter the OS type(Linux/Windows) : ')
        if (os_type =='Linux') | (os_type =='Windows'):
            d=1
    del d
    with open(f'{pwd}/AWS/files/ami-ids.json','w+') as fr:
        data=json.load(fr)
        sr_no=1+data["Images"][0][os_type][-1]["Sr. No."]
        image_name=input('Enter the image name : ')
        image_id=input('Enter the image id : ')
        new_entry={     "Sr. No.": sr_no,
					"Name" : image_name,
					"ami-id" : image_id
                    }
        if new_entry in data["Images"][0][os_type]:
            print('Entry already in file......')
            del pwd,data,fr,sr_no
            os.system('clear')
            return [image_id,image_name]
        else:
            data["Images"][0][os_type].append(new_entry)
            fr.write(data)
        fr.close()
    del pwd,data,fr,sr_no
    os.system('clear')
    return [image_id,image_name]
