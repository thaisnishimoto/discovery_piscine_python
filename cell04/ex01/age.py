#!/usr/bin/env python3

str_age = input("Please tell me your age: ")

if str_age.isdigit():
	print(f"You are currently {str_age} years old.")
	added_years = 10
	while added_years <= 30: 
		num_age = int(str_age)
		print(f"In {added_years} years, you'll be {num_age + added_years} years old.")
		added_years += 10
else:
	print("Error. Enter valid numbers only.")
