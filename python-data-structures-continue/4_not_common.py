#!/usr/bin/python3
def not_common_elements(a, b):
	temp_set = a.union(b)
	final_set = set(temp_set)
	for i in temp_set:
		if i in a and i in b:
			final_set.remove(i)
	return final_set

if __name__=="__main__":
    set_a = { "API", "requests", "Selenium", "Python", "Behave"}
    set_b = { "Selenium", "Java", "Cucumber", "Maven", "API"}
    element = not_common_elements(set_a, set_b)
    [print(x) for x in sorted(list(element))]
