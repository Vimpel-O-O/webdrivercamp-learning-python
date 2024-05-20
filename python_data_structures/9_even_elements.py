#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]
my_tuple = []

for i in my_list:
	if i%2==0:
		my_tuple.append(True)
	else:
		my_tuple.append(False)
print(my_list)
my_tuple = tuple(my_tuple)
print(my_tuple)
