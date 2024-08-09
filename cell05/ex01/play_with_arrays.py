#!/usr/bin/env python3

import array

orig_arr = array.array('i', [2, 8, 9, 48, 8, 22, -12, 2])
new_arr = array.array('i') 

for value in orig_arr:
	new_arr.append(value + 2)

print(f"Original array: {orig_arr.tolist()}")
print(f"New array: {new_arr.tolist()}")
