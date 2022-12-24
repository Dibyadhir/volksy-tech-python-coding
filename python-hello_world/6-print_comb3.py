#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i == 1 and j == 2:
            print("12")
        elif i < j:
            print('{:d}{:d}' .format(i, j), end = ", ")`
