#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    word = sys.argv[1]
    prompt = input("What was the parameter? ")

    if word == prompt:
        print("Good job!")
    else:
        print("Nope, sorry...")
