#!/usr/bin/python3
def map_list(list_=[], num=0):
	def multiply(list_num):
		return list_num * num
	return list(map(multiply, list_)) 
if __name__=="__main__":
    list_ = [5, 4, 3, 2, 1, 7]
    new_list = map_list(list_, 4)
    print(f"Original: {list_}")
    print(f"Modified: {new_list}")
