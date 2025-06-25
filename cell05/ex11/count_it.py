#!/usr/bin/env python3

import sys
words = sys.argv[1:]

if len(words) == 0:
    print("none")
else:
    print(f"parameters: {len(words)}")
    for i in words:
        print(f"{i}: {len(i)}")