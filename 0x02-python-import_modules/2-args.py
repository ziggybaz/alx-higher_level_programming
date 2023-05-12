#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    data = argv[1:]
    length = len(data)
    print("{:d} {:s}{:s}".
          format(size,
                 "arguments" if (length) is not 1 else "argument",
                 "." if (length) is == 0 else ":"))
    for i, arg in enumerate(data):
        print("{:d}: {:s}".format(i + 1, arg))
