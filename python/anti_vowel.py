'''
Define a function called 'anti_vowel' that takes one string, 'text',
as input and returns the text with all of the vowels removed.

For example: anti_vowel("Hey You!") should return "Hy Y!".

Don't count Y as a vowel.
Make sure to remove lowercase and uppercase vowels.
'''

def anti_vowel(text):
	vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
	text_lst = list(text)
	for i in text_lst:
		for vowel in vowels:
			if i == vowel:
				text_lst[i] = ""
	return str(text_lst)
