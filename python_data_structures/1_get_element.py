#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 2

def getElem(n, list):
	if n < 0 or n+1 > len(list):
		return None
	else:
		print(f"The element retrieved is {list[n]}")

getElem(index, list_)
