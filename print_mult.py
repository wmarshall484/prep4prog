#!/usr/bin/env python

import sys

try:
    num = int(sys.argv[1])
except Exception as error:
    print(repr(error))
    print "Takes 1 positive numerical argument"
    raise
if not (num >= 1 and num <= 14):
    raise ValueError("Number must be >= 1 and <= 14")
nums = [x for x in range(1, num + 1)]
table = [[x*it for x in nums] for it in nums]

for i in table:
    print i
