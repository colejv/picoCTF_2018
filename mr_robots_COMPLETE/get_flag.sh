#!/bin/bash

curl -s "2018shell.picoctf.com:60945/65c0c.html" | grep -oE "picoCTF{.*}"
