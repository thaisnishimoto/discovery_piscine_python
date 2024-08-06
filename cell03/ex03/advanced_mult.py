#!/usr/bin/env python3

import sys

if len(sys.argv) != 1:
	print("none")
else:
	num = 0
	while num <= 10:
		table = []
		mult = 0
		while mult <= 10: 
			table.append(num * mult)
			mult += 1
		str_table = map(str, table)
		print(f"Table de {num}: {' '.join(str_table)}")
		num += 1
