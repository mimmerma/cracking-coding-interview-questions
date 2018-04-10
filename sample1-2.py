# 1.2 Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other

# assume permutation comparison is case sensitive
# assume whitespace is significant

# time: O(nlog(n)), where n is max(len(foo1), len(foo2))
# b/c time for sorting algorithm
# space: ?
# b/c space for sorting algorithm (in place?)

def check_permutation(foo1, foo2):
	# strings of different len cannot be permutations
	if len(foo1) != len(foo2):
		return False

	return ''.join(sorted(foo1)) == ''.join(sorted(foo2))

def tests():
	assert check_permutation('god', 'dog')
	assert not check_permutation('hello', 'goodbye')
	print('tests pass')

tests()