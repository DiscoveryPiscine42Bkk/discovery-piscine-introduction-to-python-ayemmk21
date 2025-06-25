#!/usr/bin/env python3

import sys
words = sys.argv[1:]

if len(words) <= 1:
    print("none")
else:
    result = words[::-1]
    for i in result:
        print(i)