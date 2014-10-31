'''
The median is the middle number in a sorted sequence of numbers.

Finding the median of [7,12,3,1,6] would first consist of 
sorting the sequence into [1,3,6,7,12] and then locating the 
middle value, which would be 6.

If you are given a sequence with an even number of elements, you 
must average the two elements surrounding the middle.

For example, the median of the sequence [7,3,1,4] is 3.5, since 
the middle elements after sorting the list are 3 and 4 and 
(3 + 4) / (2.0) is 3.5.

You can sort the sequence using the sorted() function, like so:

sorted([5, 2, 3, 1, 4])

Instructions

Write a function called median that takes a list as an input and
returns the median value of the list.

For example: median([1,1,2]) should return 1.

The list can be of any size and the numbers are not guaranteed 
to be in any particular order.

If the list contains an even number of elements, your function 
should return the average of the middle two.
'''

def median(numbers):
    numbers = sorted(numbers)
    if len(numbers) % 2 == 0:
        center_right = len(numbers) / 2
        center_left = center_right - 1
        return (float(numbers[center_right]) + float(numbers[center_left])) / 2
    else:
        return numbers[len(numbers) / 2]
