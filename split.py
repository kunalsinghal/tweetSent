#!/usr/bin/env python

import random

original = open("original.csv", "r")

training = open("training.csv", "w")
heldout = open("heldout.csv", "w")
testing = open("testing.csv", "w")

total = 1600000
a = 8 * total / 10
b = total / 10
c = total / 10


print a, b, c

for line in original:
    r = random.randint(0, total-1)
    total -= 1
    if r < a:
        training.write(line)
        a -= 1
    elif r < a + b:
        heldout.write(line)
        b -= 1
    else:
        testing.write(line)
        c -= 1

print a, b, c
        
original.close()
training.close()
heldout.close()
testing.close()

