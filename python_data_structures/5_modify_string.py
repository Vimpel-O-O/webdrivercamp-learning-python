#!/usr/bin/python3
string = """AbraCadabra
A new string voila!"""
def remove_char(some_string):
	stringTemp = ""
	for i in string:
		if i.lower() != "a":
			stringTemp+=i
		else:
			continue
	some_string=stringTemp
	print(some_string)

remove_char(string) 
