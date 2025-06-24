#!/usr/bin/env python3

prompt = input()
new = ""
for i in prompt:
    if i.islower():
        new += i.upper()
    elif i.isupper():
        new += i.lower()
    else:
        new += i
print(new)