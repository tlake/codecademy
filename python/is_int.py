'''
An integer is just a number without a decimal part (for instance, 
-17, 0, and 42 are all integers, but 98.6 is not).

For the purpose of this lesson, we'll also say that a number with 
a decimal part that is all 0s is also an integer, such as 7.0.

This means that, for this lesson, you can't just test the input to 
see if it's of type int.
'''

def is_int(x):
    if (x + 1) / int(x + 1) == 1:
        return True
    else:
        return False
