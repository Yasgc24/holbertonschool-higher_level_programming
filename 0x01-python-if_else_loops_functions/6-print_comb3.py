#!/usr/bin/python3
for a in range(10):
    for b in range(10):
        if a < b and a != 8:
            print(f"{a}{b}", end=', ')
        if a < b and a == 8:
            print(f"{a}{b}")
