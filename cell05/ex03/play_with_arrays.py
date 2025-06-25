#!/usr/bin/env python3

list1 = [2, 8, 9, 48, 8, 22, -12, 2]
set1 = set(list1)
result = set(i+2 for i in set1 if i > 5)
print(result)