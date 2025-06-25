#!/usr/bin/env python3

import sys
words = sys.argv[1:]

if len(words) == 0:
    print("none")
else:
    for i in words:
        if i.endswith("ism"):
            continue
        else:
            print(i + "ism")
