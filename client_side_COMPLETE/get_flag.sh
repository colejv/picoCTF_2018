#!/bin/bash

curl -s "http://2018shell.picoctf.com:55790/" | head -n 20 | cut -d "'" -f2 | tail -n 8 | tac| tr -d "\n" 

# Getting the web page, first 20 lines, then cuttin out the "'", the only taking the last 8 lines; then reversing them (tac); then
# removing the new line character "\n"
