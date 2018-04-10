# sample1-1 alternative solution - no additional data structures

# another solution might involve sorting the chars in foo, then comparing adjacent chars
# time complexity of sorting: O(nlog(n))
# time complexity of adjacent comparisons (traverse string): O(n)
# time complexity total: O(nlog(n))
# sorting might increase the space complexity

# time complexity: O(n^2)
# ???
# (n-1)+(n-2)+(n-3)...+1 ~= n^2
# b/c nested for loop for comparing each char to every other
# space complexity: O(n)
# b/c allocating memory for input string

import re

def is_unique(foo):
	# remove spaces
	foo = re.sub('\s', '', foo)

	# compare every char in foo to every other char in foo
	for i, char1 in enumerate(foo[:-1]):
		for char2 in foo[i+1:]:
			if char1 == char2:
				return False
	
	return True

def tests():
	assert is_unique('is unqe')
	assert not is_unique('is not unique')
	print('tests pass')

tests()