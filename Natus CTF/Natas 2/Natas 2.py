import re
import requests
user = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'
url = 'http://{}.natas.labs.overthewire.org/files/users.txt'.format(user)
r = requests.get(url, auth=(user, password)).text
print(re.findall('natas3:(.*)',r)[0])