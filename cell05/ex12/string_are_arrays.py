#!/usr/bin/env python3

import sys
words = sys.argv[1:]

if len(words) == 0:
    print("none")
else:
    text = ""
    for i in words:
        text += i
    count = text.count('z')

    if count == 0:
        print("none")
    else:
        z_count = 'z' * count
        print(z_count)
