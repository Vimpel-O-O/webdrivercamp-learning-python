#!/usr/bin/python3
def list_print(lst=[], i=0): 
	result = ""
	num = 0
	try:
		for n in range(i):
			result += str(lst[n])
			num = n
		print(result)
	except IndexError:
		print(result)
	return num + 1
	
if __name__=="__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7]
    count = list_print(list_, 4)
    print(f"Count: {count:d}")
    count = list_print(list_, len(list_))
    print(f"Count: {count:d}")
    count = list_print(list_, len(list_) + 2)
    print(f"Count: {count:d}")
