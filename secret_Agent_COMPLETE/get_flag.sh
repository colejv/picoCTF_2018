#!/bin/bash

curl --user-agent "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z‡ Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" -s "http://2018shell.picoctf.com:3827/flag" | grep -oE "picoCTF{.*}" > flag.txt
