# 1.3 URLify
# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the 'true' length of the string. (Note: if implementing in Java, please use a character array so that you can perform this operation in place.)

# Ex. Input: 'Mr John Smith    ', 13
#     Ouput: 'Mr%20John%20Smith'

import re

# built in py module solution
def builtIn_urlify(foo, truelen):
	# strip leading and trailing whitespace
	foo = foo.strip()
	return foo.replace(' ', '%20')

# regex solution
def regex_urlify(foo, truelen):
	foo = foo.strip()
	return re.sub('\s', '%20', foo)

def urlify(truelen):
	# set foo to modify global variable
	global foo

	# convert foo to character array
	foo = list(foo)

	spaces = 0
	for char in foo[:truelen]:
		if char == ' ':
			spaces += 1
	
	# truelen includes single spaces, each of which will be two more chars when replaced with '%20'
	i = truelen + spaces*2
	
	# tag end of char array
	if truelen < len(foo): foo[truelen] = '\0'

	for char in reversed(foo[:truelen]):
		if char == ' ':
			foo[i-1] = '0'
			foo[i-2] = '2'
			foo[i-3] = '%'
			i -= 3
		else:
			foo[i-1] = char
			i -= 1
	
	# convert char array back to string foo
	foo = ''.join(foo)

foo = 'Mr John Smith    '
def tests():
	urlify(13)
	assert foo == 'Mr%20John%20Smith'
	print('tests pass')

tests()