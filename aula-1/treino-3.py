#!/usr/bin/python3
seq = []
a, b = 0, 1
while a < 10:
    seq.append(a)
    a, b = b, a+b
print (seq)