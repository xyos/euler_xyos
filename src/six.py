#!/usr/bin/env python
square_of_sum = 0
square = 0
for i in xrange(1,101):
    square = square + i**2
    square_of_sum = square_of_sum + i
square_of_sum = square_of_sum**2
print square_of_sum - square