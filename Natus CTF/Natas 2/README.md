# Walkthrough
The html dump form the request showed a 'files' path.

![html 1](https://github.com/Oliver-Francis1997/Natas-CTF-Python/blob/main/Natus%20CTF/Natas%202/html%20dump1.PNG)

Editing the url variable to add the path showd a 'users.txt' file.

![html 2](https://github.com/Oliver-Francis1997/Natas-CTF-Python/blob/main/Natus%20CTF/Natas%202/html%20dump2.PNG)

Adding the 'users.txt' to the url reveals the password in the html dump.

![html 3](https://github.com/Oliver-Francis1997/Natas-CTF-Python/blob/main/Natus%20CTF/Natas%202/html%20dump3.PNG)

Using re.findall to filter the password out and then print it.
