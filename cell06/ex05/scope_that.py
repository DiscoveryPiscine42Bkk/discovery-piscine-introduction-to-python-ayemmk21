#!/usr/bin/env python3

def add_one(x):
    x += 1
    return

y = 3
print(f"Before function call: {y}")
add_one(y)
print(f"After function call: {y}")
