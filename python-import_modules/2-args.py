#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} arguments. ".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{} argument:" .format(len(sys.argv) - 1))
    else:
        print("{} argument:" .format(len(sys.argv) - 1))
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        print("{}: {}".format(i, sys.argv[i]))
