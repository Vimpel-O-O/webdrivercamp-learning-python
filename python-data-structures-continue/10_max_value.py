#!/usr/bin/python3
def max_value(d):
	max_key = ""
	max_val = 0
	if d == None:
		return None
	else:
		for i, j in d.items():
			if j > max_val:
				max_key = i
				max_val = j
			else:
				continue
		return max_key
			
if __name__=="__main__":
    dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
    max_key = max_value(dict_)
    print(f"Max number - {max_key}")
    max_key = max_value(None)
    print(f"Max number - {max_key}")
