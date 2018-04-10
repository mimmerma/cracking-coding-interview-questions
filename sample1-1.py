# 1.1 Is Unique
# Implement an alorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

#>>> chr(97)
#'a'
#>>> ord('a')
#97

# assume ASCII character set with 128 characters
# assume excluding spaces

import re

def is_unique(foo):
	# remove spaces
	foo = re.sub(r'\s', '', foo)

	# if len of foo greater than total ASCII chars, return False
	if len(foo) > 128:
		return False

	# create array of booleans representing whether the character at index ord(char) has been found
	# assign all False values to initial array
	char_found = [False]*128

	for char in foo:
		if char_found[ord(char)]:
			return False
		char_found[ord(char)] = True
	
	return True

# tests
def tests():
	assert is_unique('is unqe')
	assert not is_unique('is not unique')
	print('tests pass')

tests()