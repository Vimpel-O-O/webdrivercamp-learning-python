#!/usr/bin/python3
def calc_weight(list_=[]):
	if len(list_) == 0:
		return 0
	
	part1 = 0
	part2 = 0

	for i, j in list_:
		part1 += i * j
		part2 += j

	return part1 / part2
if __name__=="__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
