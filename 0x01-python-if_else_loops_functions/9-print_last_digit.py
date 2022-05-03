#!/usr/bin/python3
def print_last_digit(number):
    lastdig = number % 10
    if number < 0:
        lastdig = (number * -1) % 10
    print(lastdig, end='')
    return lastdig
