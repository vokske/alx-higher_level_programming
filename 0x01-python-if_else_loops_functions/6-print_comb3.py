#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        print("{}{}".format(i, j), end=", " if i < 0 or j < 0 else "\n")
