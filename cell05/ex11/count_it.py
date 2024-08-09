#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
	print("none")
else:
	params = sys.argv[1:]
	print(f"parameters: {len(params)}")
	for item in params:
		print(f"{item}: {len(item)}")
