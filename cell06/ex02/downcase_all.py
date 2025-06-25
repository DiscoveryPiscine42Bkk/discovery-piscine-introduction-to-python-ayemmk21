#!/usr/bin/env python3

import sys

def downcase(x):
    return x.lower()

words = sys.argv[1:]
if len(words) == 0:
    sys.exit("none")
else:
    for i in words:
        print(downcase(i))



