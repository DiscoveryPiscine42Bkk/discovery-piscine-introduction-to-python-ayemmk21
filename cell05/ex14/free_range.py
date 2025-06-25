#!/usr/bin/env python3

import sys
words = sys.argv[1:]

if len(words) != 2:
    print("none")
else:
    first = int(words[0])
    last = int(words[-1])
    result = [i for i in range(first,last+1,1)]
    print(result)