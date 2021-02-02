import re
import requests
user = 'natas0'

url = 'http://{}.natas.labs.overthewire.org'.format(user)
r = requests.get(url, auth=(user, user)).text
#print(re.findall('<!--The password for natas1 is (.*) -->', r)[0])
print(r)