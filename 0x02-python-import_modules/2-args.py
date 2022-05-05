#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    alen = len(argv)
    if alen == 1:
        print(f"{alen - 1} arguments.")
    elif alen == 2:
        print(f"{alen - 1} argument:")
    else:
        print(f"{alen - 1} arguments:")
    for arguments in range(1, alen):
        print(f"{arguments}: {argv[arguments]}")
