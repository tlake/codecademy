pyg = 'ay'

# Let's put in a debug switch:
debug = raw_input("Enter 'y' for debug messages:")

# Getting user input:
original = raw_input('Enter a word:')

# Let's make sure that we apply our efforts only to appropriate alphabetic inputs:
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:len(word)] + first + pyg
    if debug == "y" or debug == "'y'":
        print "Original:", original
        print "Word:", word
        print "First:", first

    print "New Word:", new_word
    
else:
        # This is what happens if we don't get something good to play with.
    print 'Input was empty or contained non-alphabetical characters.'
