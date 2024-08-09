#!/usr/bin/env python3

from sys import argv

if len(argv) < 2:
	print("none")
else:
	for arg in argv[1:]:
		if arg.endswith("ism"):
			continue
		else:
			print(arg + "ism") 
