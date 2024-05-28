#!/usr/bin/python3
def dict_v_delete(a_dictionary, value):
	if value in a_dictionary.values():
		dict_chng = a_dictionary.copy()
		for i, j  in dict_chng.items():
			if j == value:
				del a_dictionary[i]
	return a_dictionary

if __name__=="__main__":
    dict_print = __import__('6_dict_print').dict_print
    dict_ = {"libs": (1,2,3), "x": "Selenium", "lang": ["Java"], "frame": "Selenium"}
    new_dict = dict_v_delete(dict_, "Selenium")
    print(f"{'Updated Dict':.^20}")
    dict_print(new_dict)
    new_dict = dict_v_delete(dict_, 'y')
    print(f"{'Updated Dict':.^20}")
    dict_print(new_dict)
