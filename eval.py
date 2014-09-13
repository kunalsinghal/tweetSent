from ast import literal_eval as eval
import re

class Classify:
    def __init__(self):
        _pos = file("pos", "r")
        _neg = file("neg", "r")
        self.pos = eval(_pos.readline().strip())
        self.neg = eval(_neg.readline().strip())
        _pos.close()
        _neg.close()
    def classify(self, line):
        def score(dic, s):
            if s in dic:
                return dic[s] + 1
            else:
                return 1
            
        lis = re.sub('([\d\.\'\"]+?)|(@[^\s]+?)','', line.replace(',',' ')).lower().split()
        P_pos = 1
        P_neg = 1
        for x in lis:
            P_pos *= score(self.pos, x)
            P_neg *= score(self.neg, x)
        return P_pos > P_neg