#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    lena = len(argv)
    resl = 0

    for n in range(1, lena):
        resl += int(argv[n])
    print(resl)
