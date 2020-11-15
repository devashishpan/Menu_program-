#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess as sp

def set_ingress(sg_id):
    os.system('clear')

    print('Finding Your Public IP.........')
    i=1
    while(i!=0):
        ip=sp.getoutput('curl "https://checkip.amazonaws.com/"')
        ip=ip.split('\n')
        ip=ip[-1]
        if ip.find('curl: (6) Could not resolve host: checkip.amazonaws.com')!=-1:
            print('Check Your internet connection.........')
            input('Press enter to continue......')
        else:
            i=0
    print('Adding Your Public IP to Your Security Group....')
    os.system(f'aws ec2 authorize-security-group-ingress --group-id {sg_id} --protocol tcp --port 22 --cidr {ip}/24')
    print('Your Public IP has been added....')
    print('Your Updated Security Group Details....')
    os.system(f'aws ec2 describe-security-groups --group-ids {sg_id}')
    input('Press enter to continue....')
    os.system('clear')
#set_ingress("sg-01886ab2810b75818")
