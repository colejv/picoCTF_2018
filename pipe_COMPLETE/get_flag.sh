#!/bin/bash

nc 2018shell.picoctf.com 37542 | grep -oE "picoCTF{.*}"
