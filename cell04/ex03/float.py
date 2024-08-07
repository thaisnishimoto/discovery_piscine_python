#!/usr/bin/env python3

num = input("Give me a number: ")

try:
	int_value = int(num)
	print("This number is an integer.")
except ValueError:
	try:
		float_value = float(num)
		if float_value.is_integer():
			print("This number is an integer.")
		else:
			print("This number is a decimal.")
	except ValueError:
		print("Error. Enter numbers only.")
