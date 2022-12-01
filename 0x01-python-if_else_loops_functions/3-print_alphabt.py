#!/usr/bin/python3
for letters in range(26):
    if letters != 4 and letters != 16:
        print("{:s}".format(chr(letters + ord("a"))), end="")
