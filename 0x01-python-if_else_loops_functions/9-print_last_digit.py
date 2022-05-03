#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastdig = -1 * (-number % 10)
    print(f"{lastdig}", end='')
    return lastdig
