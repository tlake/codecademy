def reverse(text):
	new_string = ""
	for i in range(len(text)):
		new_string += text[(len(text) - 1) - i]
	return new_string

print reverse("abcd")
