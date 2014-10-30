'''
Define a function called 'is_prime' that takes a number 'x' as input.

For each number n from 2 to x - 1, test if x is evenly divisible by n.

If it is, return False.

If none of them are, then return True.
'''

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        truth_storage = 0
        for i in range(2, x):
            if x % i == 0:
                truth_storage += 1
        if truth_storage == 0:
            return True
        else:
            return False
