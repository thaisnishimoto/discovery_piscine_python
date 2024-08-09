#!/usr/bin/env python3

from sys import argv

if len(argv) != 2:
	print("none")
else:
	z_count = argv[1].count('z')
	if z_count == 0:
		print("none")
	else:
		print('z' * z_count)
