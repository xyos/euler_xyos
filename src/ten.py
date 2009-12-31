#!/usr/bin/env python
from seven import prime
def sumprim(num):
    sum = 2
    for i in xrange(3,num+1):
        if prime(i):
            sum = sum+i
    print sum

sumprim(2000000)

