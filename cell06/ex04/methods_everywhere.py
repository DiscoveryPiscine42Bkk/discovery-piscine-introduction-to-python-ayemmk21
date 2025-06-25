#!/usr/bin/env python3

import sys
words = sys.argv[1:]

def shrink(x):
    print(x[:8])

def enlarge(x):
    for i in range(len(x),8):
        x += 'Z'
    print(x)

if len(words) == 0:
    print("none")
else:
    for j in words:
        if len(j) < 8:
            enlarge(j)
        elif len(j) > 8:
            shrink(j)
        else:
            print(j)

