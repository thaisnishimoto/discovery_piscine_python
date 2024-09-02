#!/usr/bin/env python3

from sys import argv

def downcase_it(string):
	return string.lower()

if len(argv) == 1:
	print("none")
else:
	for arg in argv[1:]:
		print(downcase_it(arg))
