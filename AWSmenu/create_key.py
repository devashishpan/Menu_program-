import os,subprocess,json
def create_key():
    os.system('clear')
    pwd=subprocess.getoutput('pwd')
    MyKeyPair=input('Enter Your Key-Pair name ; ')
    os.system(f'aws ec2 create-key-pair --key-name {MyKeyPair} --query \'KeyMaterial\' --output text > {pwd}/AWS/files/keys/{MyKeyPair}.pem')
    print(f'Key Pair {MyKeyPair}.pem is created.....')
    print('Securing your key..........')
    os.system(f'chmod 400 {pwd}/AWS/files/keys/{MyKeyPair}.pem')
    update_key_file()
    print('Completed.......')
    del pwd,MyKeyPair
def find_key():
    update_key_file()
    os.system('clear')
    pwd=subprocess.getoutput('pwd')
    with open(f'{pwd}/AWS/files/keys/key_details.json','r') as fr:
        data=json.load(fr)
        fr.close()
    try:
        choice=0
        while(choice!=-1):
            print('Listing all keys on the system :.....')
            j=1
            for i in data["KeyPairs"]:
                print(f'\t{j} . {i["KeyName"]} : {i["Tags"]}')
                j+=1
            try:
                choice=int(input('Enter the serial number of the desired Key: '))
            except:
                print('Enter a valid choice...')
            if choice<=0 | choice>j:
                input('Press enter to continue...')
                os.system('clear')
            else:
                print('Your choice : ')
                i=data["KeyPairs"][choice-1]
                print(f'\t{i["KeyName"]} : {i["Tags"]}')
                print('Detailed Description:::---------------------------------')
                os.system(f'aws ec2 describe-key-pairs --key-name {i["KeyName"]}')
                con=input('\nConfirm Your Choice(y/n):')
                if con=='y':
                    choice=-1
                    sch=i["KeyName"]
                    del data,j,i
                else:
                    choice=0
        del choice,pwd,fr
        os.system('clear')
        return sch
    except:
        print('No keys created or key-details files Missing....\n Create a key....')
        input('Press enter to continue........')
        os.system('clear')
        create_key()
def update_key_file():
    os.system('clear')
    pwd=subprocess.getoutput('pwd')
    with open(f'{pwd}/AWS/files/keys/key_details.json','w') as fw:
        data=subprocess.getoutput('aws ec2 describe-key-pairs')
        fw.write(data)
        fw.close()
        print('Key-Details file updated.....')
    del fw,pwd,data
