import numpy
from scipy import *
from scipy.sparse import *
from sklearn import svm
import re
import sys
from nltk.corpus import stopwords
from ast import literal_eval as eval
import cPickle as pickle

# class Classify:
#     def __init__(self):
#     	_words = file('words', 'r')
#     	self.words = eval(_words.readline().strip())
#     	_words.close()
#     	training = file('training.csv', 'r')
#     	cols = len(self.words)
#     	rows = 1280000
#     	features = dok_matrix((rows,cols), dtype=bool)
#     	y = [0 for x in xrange(rows)]
#     	i = 0
#     	for line in training:
# 			lis = re.sub('[^#\sa-zA-Z]+?', '', re.sub('@[^\s]+?','', line.replace(',',' '))).lower().split()
# 			for x in lis:
# 				if x in self.words:
# 					# print i, self.words[x]
# 					# print rows, cols
# 					# print '----'
# 					features[i, self.words[x]] = 1
# 			y = line[1]
#     	training.close()
#     	print "features stored"
#     	linear_classifier = svm.LinearSVC()
#     	print "classifier created"
#     	linear_classifier.fit(features, y)
#     	print "classifier fitted"

# x = Classify()


_words = file('words', 'r')
words = eval(_words.readline().strip())
_words.close()
training = file('testing.csv', 'r')
cols = len(words)
rows = 160000
features = dok_matrix((rows,cols), dtype=bool)
y = [0 for x in xrange(rows)]
i = 0
cnt = 0
for line in training:
	cnt += 1
	lis = re.sub('[^#\sa-zA-Z]+', '', re.sub('@[^\s]+','', line.replace(',',' '))).lower().split()
	for x in lis:
		if x in words:
			# print i, self.words[x]
			# print rows, cols
			# print '----'
			features[i, words[x]] = 1
	y[cnt-1] = line[1]
	if cnt % 10000 == 0: 
		print cnt, y[cnt-1], type(y[cnt-1])
training.close()
linear_classifier = svm.LinearSVC().fit(features, y)
svm_model = file('svm_model', 'wb')
pickle.dump(linear_classifier, svm_model)
svm_model.close()

while True:
	text = raw_input()
	lis = re.sub('[^#\sa-zA-Z]+', '', re.sub('@[^\s]+','', text.replace(',',' '))).lower().split()
	print lis
	features = dok_matrix((1,cols), dtype=bool)
	for x in lis:
		if x in words:
			features[0, words[x]] = 1
	print linear_classifier.predict(features)
