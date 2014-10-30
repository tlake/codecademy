'''
Define a function 'factorial' that takes an integer 'x' as input.

Calculate and return the factorial of that number.
'''

def factorial(x):
    calc = 1
    if x > 1:
        for i in range(2, x + 1):
            calc *= i
        return calc
    elif x == 1:
        return 1
    else:
        print "I need a positive integer."
