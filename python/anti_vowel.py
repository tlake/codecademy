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
    new_list = []
    for i in text_lst:
        if i not in vowels:
            new_list += i
    return "".join(new_list)
