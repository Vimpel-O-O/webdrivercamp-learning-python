#!/usr/bin/python3
def common_elements(a, b):
	final_set = set()
	for i in a:
		if i in b:
			final_set.add(i)
	return final_set

if __name__=="__main__":
    set_a = { "API", "requests", "Selenium", "Python", "Behave"}
    set_b = { "Selenium", "Java", "Cucumber", "Maven", "API"}
    same_element = common_elements(set_a, set_b)
    [print(x) for x in sorted(list(same_element))]
