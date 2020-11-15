import os,subprocess

print('Checking for internet access.......')
c=subprocess.getstatusoutput('curl -I https://www.google.com')
if c[0]==0:
	print('You have internet access...')
	print('Starting aws installer script........')
	print('Downloading awscliv2.zip.....')
	os.system('curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"')
	print('Unzipping awscliv2.zip.....')
	os.system('unzip awscliv2.zip')
	print('Installing aws........')
	os.system('./aws/install')
	os.system('rm -d aws')
	os.system('rm awscli2.zip')
else:
	print('Connect to a network with internet connection and try again......')
os.system('clear')
print('installation complete......')
