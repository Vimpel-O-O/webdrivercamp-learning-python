#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

def repElem(n, list, repnum):
	templist = list.copy()
	if n < 0 or n+1 > len(list):
		print(list)
	else:
		templist[n]=repnum
		print(f"Copy:    {templist}")
		print(f"Original:{list}")

repElem(index, list_, element_to_replace)

