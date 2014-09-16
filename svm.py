import re
from nltk.corpus import stopwords



f = file('testing.csv', 'r')

word_count = {} 
words = {}
dic_size = 0
stop = set(stopwords.words('english')+ ['im'])

def check(x):
    if x in stop:
        return False
    return True
    
for line in f:
    lis = re.sub('[^#\sa-zA-Z]+', '', re.sub('@[^\s]+','', line.replace(',',' '))).lower().split()

    for x in lis:
        if check(x):
            if x in word_count:
                cnt = word_count[x] 
                cnt += 1
                word_count[x] = cnt
                if cnt > 10 and x not in words:
                	words[x] = dic_size
                	dic_size += 1
            else:
                word_count[x] = 1

print len(words)

f.close()

_words = file('words', 'w')


_words.write(str(words))
_words.close()
    
    


