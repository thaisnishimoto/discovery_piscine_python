#!/usr/bin/env python3

from sys import argv

if len(argv) != 3:
	print("none")
else:
	start = int(argv[1])
	end = int(argv[2]) + 1
	arr = list(range(start, end))
	print(arr)
