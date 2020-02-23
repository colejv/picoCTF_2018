#!/usr/bin/env python

import re
import requests

url = 'http://2018shell.picoctf.com:3827/flag'

# Create a user agent
user_agent = 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
headers = {'User-Agent': user_agent}

response = requests.get(url, headers=headers)

print re.findall('picoCTF{.*}',response.text)[0]