import os,subprocess,json
import AWSmenu.find_vpcs as fv
import AWSmenu.sg_ingress as si

def create_sg():
    os.system('clear')
    pwd=subprocess.getoutput('pwd')
    vpcs_id=fv.read_vpcs()
    if (vpcs_id==0):
    	vpcs_id=fv.update_vpcs()
    d=0
    while(d!=1):
        my_sg=input('Enter a name for your security group : ')
        print('Creating a new security group.....')
        data=subprocess.getoutput(f'aws ec2 create-security-group --group-name {my_sg} --description "My security group" --vpc-id {vpcs_id}')
        if (data.find('InvalidGroup.Duplicate')>-1) :
            print('Change Security Group name. Security group {my_sg} already exists.....')
            input('Press enter to continue.......')
            os.system('clear')
        else:
            print('Security Group Created.........')
            d=1
            del my_sg
            del vpcs_id
    del d
    with  open('sg_id.json','w') as fw:
        fw.write(data)
        fw.close()
        del fw
    with open('sg_id.json','r') as fr:
        data=json.load(fr)
        sg_id=data['GroupId']
        fr.close()
        del fr
        del data
    os.system('rm sg_id.json')
    print(f'SECURITY GROUP ID = {sg_id}\nSecurity Group Details...\n')
    os.system(f'aws ec2 describe-security-groups --group-ids {sg_id}')
    input('Press Enter to clear screen....')
    del pwd
    os.system('clear')
    si.set_ingress(sg_id)
def find_sg():
    pwd=subprocess.getoutput('pwd')
    os.system('clear')
    with open(f'{pwd}/AWS/files/security_groups_details.json','w') as fw:
        data=subprocess.getoutput('aws ec2 describe-security-groups')
        fw.write(data)
        fw.close()
        del fw,data
        with open(f'{pwd}/AWS/files/security_groups_details.json','r') as fr:
            data=json.load(fr)
        j=1
        choice=0
    while(choice!=-1):
        os.system('clear')
        print('Listing all Security Groups......')
        for i in data["SecurityGroups"]:
            print(f'\t{j}. {i["GroupName"]}  : {i["GroupId"]}')
            j+=1
        try:
            choice=int(input('Enter the serial number of the desired Security Group : '))
        except:
            print('Enter a valid choice...')
        if choice<=0 | choice>j:
            print('Enter a valid choice......')
            input('Press enter to continue...')
            os.system('clear')
        else:
            print('Your choice : ')
            i=data["SecurityGroups"][choice-1]
            print(f'\t{i["GroupName"]}  : {i["GroupId"]}')
            print('Detailed Description:::---------------------------------')
            os.system(f'aws ec2 describe-security-groups --group-ids {i["GroupId"]}')
            con=input('\nConfirm Your Choice(y/n):')
            if con=='y':
                choice=-1
                sch=[i["GroupId"],i["GroupName"]]
                del data,j,i
            else:
                choice=0
    del choice,pwd,fr
    si.set_ingress(sch)
    os.system('clear')
    return sch