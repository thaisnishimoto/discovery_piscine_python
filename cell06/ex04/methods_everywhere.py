#!/usr/bin/env python3

from sys import argv

def shrink(string):
	print(string[slice(8)])

def enlarge(string):
	buff = 8 - len(string)
	print(string + buff * 'Z')

if len(argv) > 1:
	for arg in argv[1:]:
		if len(arg) < 8:
			enlarge(arg)
		else:
			shrink(arg)
else:
	print("none")
