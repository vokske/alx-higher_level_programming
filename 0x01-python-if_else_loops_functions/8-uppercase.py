#!/usr/bin/python3

def uppercase(str):
    string = ""
    for ch in str:
        if 97 <= ord(ch) <= 122:
            string += chr(ord(ch) - 32)
        else:
            string += ch
    print("{}".format(string), end="")
    print()
    return string
