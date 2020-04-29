#!/usr/bin/python3
def fibonnati(max):
    seq = []
    a, b = 0, 1
    while a < max:
        seq.append(a)
        a, b = b, a+b
    return seq

print (fibonnati(10))
print (fibonnati(100))