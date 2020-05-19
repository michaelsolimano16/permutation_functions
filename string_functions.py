
#Problem: Implement an algorithm to determine if a string has all unique characters.

def stringUnique_py(input_string):
	#A function taking advantage of python:

	tracking_letters = []

	for letter in input_string:
		if letter in tracking_letters:
			print(f"{input_string} is not a set of letters.")
			return False
		tracking_letters.append(letter)

	print(f"{input_string} is a word of distinct letters.")
	return True


def stringUnique(input_string):
	#A function that doesn't take advantage of Python if:
	#Assume letter_tracker acts as a Java Arraylist

	letter_tracker = []

	for letter in input_string:
		if len(letter_tracker) > 0:
			for tracked_letter in letter_tracker:
				if letter == tracked_letter:
					print(f"{input_string} is not a set of letters.")
					return False
			letter_tracker.append(letter)
		else:
			letter_tracker.append(letter)

	print(f"{input_string} is a word of distinct letters.")
	return True

test = "exam"
test_two = "testing"
stringUnique_py(test)
stringUnique_py(test_two)