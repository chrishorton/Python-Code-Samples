def my_reverse(word):
	word = list(word)
	temp = 0

	# The last letter is the length of the [word-1]
	# the first letter is just [0]
	length = len(word)

	for i in range(length):	
		temp = word[length-i-1]
		word[length-i-1] = word[i]
		word[i] = temp
		if i==(length/2):
			break


	return word

chris.horton@sbcglobal.net

my_word = "dog"
reversed_word = my_reverse(my_word)
print (reversed_word)