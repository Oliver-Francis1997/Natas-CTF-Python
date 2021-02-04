import re
import requests
import html

user = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
url = 'http://{}.natas.labs.overthewire.org/'.format(user)
data = {'secret' : 'oubWYf2kBq', 'submit' : ''}
r = requests.Session().post(url, data= data, auth=(user, password)).text
print(re.findall('natas9 is (.*)', r)[0])