import re
import sys
from nltk.corpus import stopwords
f = file('training.csv', 'r')

neg = {}
pos = {}

stop = set(stopwords.words('english')+ ['im'])

def check(x):
    if x in stop:
        return False
    return True
    
for line in f:
    if line[1] == '0':
        hash = neg
    else:
        hash = pos
    lis = re.sub('[^#\sa-zA-Z]+', '', re.sub('@[^\s]+','', line.replace(',',' '))).lower().split()

    for x in lis:
        if check(x):
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

    
    

