#!/usr/bin/python3
def fibonnati():
    seq = []
    a, b = 0, 1
    while a < 10:
        seq.append(a)
        a, b = b, a+b
    return seq

print (fibonnati())