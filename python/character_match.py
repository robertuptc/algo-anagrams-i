# Don't forget to run your tests!

from operator import index, indexOf, truediv
import string


def is_character_match(string1, string2):
	list1 =list(string1.lower().replace(" ",""))
	list2 = list(string2.lower().replace(" ", ""))

	word_list1 = []
	word_list2 = []

	x = len(list1)
	while x > 0 :
		word_list1.append(max(list1))
		list1.pop(list1.index(max(list1)))
		x = x-1

	y = len(list2)
	while y > 0 :
		word_list2.append(max(list2))
		list2.pop(list2.index(max(list2)))
		y = y-1

	return "".join(word_list1) == "".join(word_list2)






