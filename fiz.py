#!/usr/bin/env python
import sys

def printSumToN(n):
    sum = 0
    for val in range(1, n+1):
        if val % 3 == 0 or val % 5 == 0:
            sum += val
    print sum

if len(sys.argv) != 2:
    print "fiz.py takes 1 positive integer argument"
printSumToN(int(sys.argv[1]))
