#!/usr/bin/env python3

import array

orig_arr = array.array('i', [2, 8, 9, 48, 8, 22, -12, 2])
new_arr = array.array('i') 

for value in orig_arr:
	if value > 5:
		new_arr.append(value + 2)

print(f"{orig_arr.tolist()}")
print(f"{new_arr.tolist()}")
