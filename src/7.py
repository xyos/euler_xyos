#!/usr/bin/env python
from math import sqrt

def prime(num):
    pri=True
    for i in xrange (2,int(sqrt(num)+1)):
        if num % i == 0:
            pri=False
            break
    return pri

def count(num):
    count = 1
    prim = 2
    while (count!= num):
        prim = prim + 1
        if prime(prim):
            count = count+1
    print prim
    
count(10001)
    