'''
Define a function called 'reverse' that takes a string 'text'
and returns that string in reverse.

For example: reverse("abcd") should return "dcba".

You may not use 'reversed' or '[::-1]' to help you with this.
You may get a string containing special characters 
(for example, !, @, or #).
'''

def reverse(text):
	text = str(text)
	new_string = ""
	for i in range(len(text)):
		new_string += text[(len(text) - 1) - i]
	return new_string
