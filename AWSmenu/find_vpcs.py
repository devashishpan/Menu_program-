#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json,os,subprocess

def read_vpcs():
    pwd=subprocess.getoutput('pwd')
    try:
        with open(f'{pwd}/AWS/files/vpcs.json','r') as fr:
            data=json.load(fr)
            fr.close()
            del fr
            vpcs_id=data['Vpcs'][0]['VpcId']
            del data
            return vpcs_id
    except:
        return 0
def update_vpcs():
    pwd=subprocess.getoutput('pwd')
    with open(f'{pwd}/AWS/files/vpcs.json','w') as fw:
        fw.write(subprocess.getoutput('aws ec2 describe-vpcs'))
        fw.close()
        del fw
