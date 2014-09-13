import re
import sys

f = file('training.csv', 'r')

neg = {}
pos = {}

for line in f:
    if line[1] == '0':
        hash = neg
    else:
        hash = pos
    lis = re.sub('([\d\.\'\"]+?)|(@[^\s]+?)','', line.replace(',',' ')).lower().split()
    for x in lis:
        if x in hash:
            hash[x] += 1
        else:
            hash[x] = 1

f.close()

_pos = file('pos', 'w')
_neg = file('neg', 'w')

_pos.write(str(pos))
_pos.close()
_neg.write(str(neg))
_neg.close()

    
    

