import sys
import re

def exists(x):
    if x:
        return True
    return False

def URL(x):
    return exists(re.match('(https?://)?([\w-]+\.)?[\w-][\w-]+(\.co)?\.[a-z-]{2,4}(/[^\"\'\(\)]+)*/?', x))

def Smiley(x):
    return exists(re.match('[:;=][oO\-~]?[PDpdoO\\\)\]]', x))

def Hyphen(x):
    for c in x:
        if not (c.isalnum() or c == '-'):
            return False
    return x.count('-') == 1 and len(filter(None, x.split('-'))) == 2

def Number(x):
    for c in x:
        if not c in ([str(i) for i in xrange(10)] + [',', '.']):
            return False
    var = re.match('([0-9]+[\.,])*[0-9]+', x)
    if exists(var) :
        a, b = var.span()
        return len(x) == (b-a)
    return False

def Mention(x):
    var =  re.match('@[\w-]+', x)
    if var:
        a, b = var.span()
        return len(x) == (b-a)
    return False

def Hash(x):
    var =  re.match('#[\w]+', x)
    if var:
        a, b = var.span()
        return len(x) == (b-a)
    return False

def isDateTime(x):
    return "CSL772" in x

def getTime(x ,y):
    x %= 24
    if x < 10:
        return "0" + str(x * 100 + y)
    return str(x*100 + y)

def getDate(a, b, c):
    if len(c) == 2:
        if int(c) < 20: 
            c = "20" + c
        else : 
            c = "19" + c
    if int(a) > 12:
        a,b = b,a
    if len(a) == 1:
        a = "0" + a
    if len(b) == 1:
        a = "0" + a 
    return c+"-" + a + "-" + b

def getDateWord(a, b, c):
    if len(c) == 2:
        if int(c) < 20: 
            c = "20" + c
        else : 
            c = "19" + c
    a = months[a.lower()]
    if len(b) == 1:
        a = "0" + a
    return c+"-" + a + "-" + b 



for line in sys.stdin:
    sent = line[1]
    line = line[5:-1]
    line = line.replace("RT@","RT @")
    # line = line.replace("'s", " 's")
    line = re.sub("'s ([a-zA-Z]*een) ", " has \\1 ", line, re.I)
    line = line.replace(',', ' , ')
    line = line.replace("'m", " am")
    line = line.replace("'d", " would")
    line = line.replace("'ve", " have")
    line = line.replace("'ll", " will")
    line = line.replace("'s", " is")                # but how to differentiate from possessive
    line = line.replace("'re", " are")
    line = line.replace("cant", "can not")
    line = line.replace("can't", "can not")
    line = line.replace("wont", "would not")
    line = line.replace("won't", "would not")
    line = line.replace("n't", " not")              # any more cases for not? 
    line = line.replace("y'all", "you all")
    
    line = re.sub('([:;=][oO\-~]?[PDpdoO\\\)\]])', ' \\1 ', line) # horizontal face smileys
    line = re.sub('((https?://)?([\w-]+\.)?[\w-][\w-]+(\.co)?\.[a-z-]{2,4}(/[^\s\"\'\(\)]+)*(/|(\?[^\s\"\'\(\)]+))?)([^\w])', ' \\1 \\8', line, re.I) # this is for urls
    line = re.sub('(@[\w-]+)', "\\1 ", line) #mentions
    line = re.sub('(#[\w]+)', "\\1 ", line) #hashtags 


    line = re.sub("'(.+?)'", "' \\1 '", line)       # single quotes
    line = re.sub('"(.+?)"', '" \\1 "', line)       # double quotes
    line = re.sub(" (([0-9]+[\.,])*[0-9]+)", " \\1 ", line)

    final = [] 
    line
    

    for x in line.split():
        if URL(x) or Smiley(x) or Number(x) or Mention(x) or Hash(x) or isDateTime(x):
            None
        else:
            if x.count('.') == 1:
                x = x.replace('.', ' . ')
            else:
                x = re.sub('(\.\.+)', ' \\1 ', x)       # handles .. , ... etc
            x = re.sub('([\?!]+)', ' \\1 ', x)      # handles !?!!?
            x = re.sub('("+)', ' \\1 ', x)          # handles random double quotes
            x = re.sub('(\'\'+)', ' \\1 ', x)       # handles random single quotes
            x = re.sub('(&+)', ' \\1 ', x)
            x = re.sub('(\$\$+)', ' \\1 ', x)
            x = re.sub('(\\+)', ' \\1 ', x)
            x = re.sub('(/+)', ' \\1 ', x)
            x = x.replace(')', ' ) ')
            x = x.replace('(', ' ( ')
            x = x.replace(';', ' ; ')
            if not Hyphen(x):
                x = re.sub('([>:<-]+)', ' \\1 ', x)      # handles arrows and hypens
            else:
                x = x.replace("-", " -")
            x = re.sub("([0-9])([a-zA-Z])", "\\1 \\2", x)
            
        final += x.split()
    
    print reduce(lambda x,y: x+' '+y, final) + "-=-=-" + sent