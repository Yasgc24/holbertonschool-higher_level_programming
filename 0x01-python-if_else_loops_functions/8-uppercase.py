#!/usr/bin/python3
def uppercase(str):
    for char in str:
        letter = ord(char)
        if letter > 96 and letter < 124:
            letter -= letter
        print(char(letter), end='')
    print()

