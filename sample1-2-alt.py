# 1.2 Check Permutation - alt solution
# definition of permutation - two words with same char count

# len(unicode character set)?

# time: O(n), where n is max(len(foo1), len(foo2))
# b/c iterate through each string building character frequency array
# space: O(c), where c is len(character set)
# b/c allocate chatacter frequency array

def check_permutation(foo1, foo2):
	# must be same len
	if len(foo1) != len(foo2):
		return False

	# assume ASCII character set, len 128
	char_freq = [0]*128
	for char in foo1:
		char_freq[ord(char)] += 1
	
	for char in foo2:
		char_freq[ord(char)] -= 1
		# if any values neg, then fewer of at least one char in foo1 than foo2
		if char_freq[ord(char)] < 0:
			return False
	
	# input strings are same length, so if no neg values, no pos values (num of neg values must equal num of pos values)
	return True

def tests():
	assert check_permutation('dog', 'god')
	assert not check_permutation('hello', 'goodbye')
	print('tests pass')

tests()