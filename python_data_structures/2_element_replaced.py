#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

def repElem(n, list, repnum):
	if n < 0 or n+1 > len(list):
		print(list)
	else:
		list[n]=repnum
		print(list)

repElem(index, list_, element_to_replace)
