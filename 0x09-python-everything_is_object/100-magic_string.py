#!/usr/bin/python3
def magic_string(n):
    return "\n".join(", ".join(["BestSchool"] * i) for i in range(1, n + 1))
