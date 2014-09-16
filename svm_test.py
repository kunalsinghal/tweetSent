import numpy
from scipy import *
from scipy.sparse import *
from sklearn import svm
import re
import sys
from nltk.corpus import stopwords
from ast import literal_eval as eval
import cPickle as pickle

_words = file('words', 'r')
words = eval(_words.readline().strip())
_words.close()
testing = file('testing.csv', 'r')
cols = len(words)
rows = 160000
features = dok_matrix((rows,cols), dtype=bool)
y = [0 for x in xrange(rows)]
i = 0
cnt = 0
for line in testing:
	cnt += 1
	lis = re.sub('[^#\sa-zA-Z]+?', '', re.sub('@[^\s]+?','', line.replace(',',' '))).lower().split()
	for x in lis:
		if x in words:
			# print i, self.words[x]
			# print rows, cols
			# print '----'
			features[i, words[x]] = 1
	y[cnt-1] = line[1]
	if cnt % 10000 == 0: 
		print cnt, y[cnt-1]
testing.close()
svm_model = file('svm_model', 'rb')
linear_classifier = pickle.load(svm_model)
svm_model.close()
yout = linear_classifier.predict(features)
score = linear_classifier.score(features, y)
print score
while True:
	text = raw_input()
	lis = re.sub('[^#\sa-zA-Z]+', '', re.sub('@[^\s]+','', line.replace(',',' '))).lower().split()
	features = dok_matrix((1,cols), dtype=bool)
	for x in lis:
		if x in words:
			features[1, words[i]] = 1
	print linear_classifier.predict(features)