from eval import Classify
import sys
#testing = file("testing.csv", "r") 
hit = 0
miss = 0
classifier = Classify()
print "Classifer loaded" 
#for line in testing:
for line in sys.stdin:
    if line[1] == '0':
        ans = False
    else:
        ans = True
    if classifier.classify(line) == ans:
        hit += 1
    else:
        miss += 1
    
#testing.close()

print "Hits:", hit
print "Miss:", miss

print "Precision:", hit * 100.0 / (hit + miss) 
