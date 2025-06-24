#!/usr/bin/env python3
password = "Python is awesome"
usr_prompt = input()
if usr_prompt != password:
    print("ACCESS DENIED.")
else:
    print("ACCESS GRANTED.")