#!/usr/bin/python3
def uppercase(str):
    for char in str:
        letter = ord(char)
        if letter > 96 and letter < 123:
            letter -= 32
        print(chr(letter), end='')
    print()
