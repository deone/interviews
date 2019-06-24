#! /usr/bin/env python

def luhn(a):
	lst = [int(i) for i in list(str(a))]
	lst.reverse()
	for i in enumerate(lst):
		if i[0] % 2 == 1:
			double = i[1] * 2
			if double > 9:
				lst[i[0]] = double - 9
			else:
				lst[i[0]] = double
	lst.reverse()
	total = sum(lst)
	if total % 10 != 0:
		return False
	return True

if __name__ == '__main__':
	print luhn(49927398716)
	print luhn(49927398717)
	print luhn(1234567812345678)
	print luhn(1234567812345670)
