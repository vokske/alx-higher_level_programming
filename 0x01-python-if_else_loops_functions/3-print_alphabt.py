#!/usr/bin/python3
for letters in range(97, 123):
    if chr(letters) not in ['e', 'q']:
        print("{}".format(chr(letters)), end="")
