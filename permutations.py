#By Michael Solimano 2020
# Problem: Given two strings, write a method to decide if one is a permutation
# of the other...

def isPermutation(string_a, string_b):
	#making use of python's sort(), this program checks for string equivalency
	if (len(string_a)) != (len(string_b)):
		#Make sure the input strings are same length
		print("These strings are not permutations of each other.")
	elif string_a == string_b:
		print("These strings are the same!")
	else:
		#sort input strings and compare sorted lists. Equivalency implies a permutation.
		sort_a = sorted(string_a)
		sort_b = sorted(string_b)
		if sort_a == sort_b:
			print("These strings are permutations!")
		else:
			print("These string are NOT permutations!")

one = "12345"
two = "54321"
isPermutation(one, two)

# Problem Two: Write a function to see if two strings are palindromes
# This method converts to lowercase letter values when checking, so is not case sensitive.

def isPalindrome(string_a, string_b):

	#Convert input strings to lower case then place their values into lists.
	#This is done because (later on), strings cannot use pop() function.
	low_a = string_a.lower()
	low_b = string_b.lower()
	lower_a = []
	lower_b = []

	for a_letter in low_a:
		lower_a.append(a_letter)
	for b_letter in low_b:
		lower_b.append(b_letter)

	#Reverse string B, so that it can be checked for equivalency with string A...
	b_length = len(lower_b)
	counter = 0
	b_reverse = []

	#Pop off the end of the b input string and append values to b_reverse.
	#This reverses the B input string.

	while counter < b_length:
		popped = lower_b.pop()
		b_reverse.append(popped)
		counter += 1

	#Now check for equivalency between 'lower-cased' string A and reverse of input string b
	if lower_a == b_reverse:
		print("Input strings are palindromes!")
	else:
		print("Input strings are NOT palindromes.")

string_one = "abcde"
string_two = "edcba"
isPalindrome(string_one, string_two)

#Problem: Implement a method for string compression: for example, aabcccccaaa will become a2b1c5a3

def stringCompressor(string_in):
	#A method to compress strings

	compressed = []
	letter_counter = 0

	#Move through the input string. If current letter is same as previous, add to array and add one rto counter
	#Else, add counter value to array then begin counting (and appending) next letter

	for letter in string_in:
		if len(compressed) > 0:
			if compressed[-1] == letter:
				counter += 1
			else:
				counter_copy = counter
				counter_copy = str(counter_copy)
				compressed.append(counter_copy)
				compressed.append(letter)
				counter = 1
		else:
			compressed.append(letter)
			counter = 1
	string_counter = str(counter)
	compressed.append(string_counter)

	#Now, take our 'compressed' list and turn it into a string.
	#This should be simple, as ints have been converted to string values already.
	assembled_word = ""
	for val in compressed:
		assembled_word += val

	#Finally, print the compressed string...
	print(assembled_word)
	

stringCompressor("aabcccccaaa")






	