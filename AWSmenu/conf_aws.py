import os,subprocess

path="/home/.aws/"
file_names=["config","credentials"]
pwd=subprocess.getoutput('pwd')
os.system(f"rm {path}{file_names[0]} {path}{file_names[1]}")

with open(f'{pwd}/AWS/files/new_user_credentials.csv', 'r') as fr:
	r=fr.readlines()
	d=r[1].split(',')

credentials=f'''[default]
aws_access_key_id = {d[2]}
aws_secret_access_key = {d[3]}'''
region=input('Enter the region id : ')
config=f'''[default]
region = {region}
output = json'''
with open(file_names[0], 'w') as fp:
	fp.write(config)
with open(file_names[1], 'w') as fp:
	fp.write(credentials)
os.system('clear')
print('Configuration complete....')
