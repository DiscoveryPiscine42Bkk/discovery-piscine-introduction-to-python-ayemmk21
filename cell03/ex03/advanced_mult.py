#!/usr/bin/env python3
first = 0

while first <= 10:
        print(f"Table de {first}:", end ="")
        second = 0
        while second <= 10:
            print(first * second, end =" ")
            second += 1
        print()
        first += 1