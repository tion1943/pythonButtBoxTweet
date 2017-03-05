import random

userIn = open('user.txt').read()
verbIn = open('verb.txt').read()
nounIn = open('noun.txt').read()

def findRand(string):
    wordList = string.split(',')
    return random.choice(wordList).strip()
loop = True
while(loop):
    user = findRand(userIn)
    verb = findRand(verbIn)
    noun = findRand(nounIn)
    
    tweet = user + ' ' + verb + ' ' + noun
    if len(tweet)>=29:
        continue
    print len(tweet)
    print tweet
    break
