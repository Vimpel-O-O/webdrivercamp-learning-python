#!/usr/bin/python3

def only_unique(list_=[]):
	n = 0
	list_ = set(list_)
	for i in list_:
		n += i
	return n


if __name__=="__main__":
    list_ = [0, 1, 6, 3, 6, 4, 0, 2, 5, 4, 4]
    result = only_unique(list_)
    print(f"Sum of unique: {result}")
