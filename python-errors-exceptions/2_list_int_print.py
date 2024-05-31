#!/usr/bin/python3
def list_int_print(lst=[], i=0):
	result = 0
	for n in range(i):
		try:
			print(f"{lst[n]:d}", end = "")
			result += 1
		except (TypeError, ValueError):
			pass
	print()
	return result

if __name__=="__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7]
    count = list_int_print(list_, 4)
    print(f"Count: {count:d}")
    list_ = [1, 2, "Camp", 5, [3, 4]]
    count = list_int_print(list_, len(list_))
    print(f"Count: {count:d}")
    count = list_int_print(list_, len(list_) + 2)
    print(f"Count: {count:d}")
