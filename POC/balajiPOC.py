import random

tweets = list()
inputs = open('../balaji.txt')
for line in inputs:
    if (line != '\n') and not(line.startswith('#')):
        tweets.append(line.strip())
tweetStr = str()        
while(True):
    frontTweet = random.choice(tweets)
    f = open('../user.txt').read()
    names = f.strip().split(',')
    name = random.choice(names)
    backTweet = name + ' what do you think about this?'
    tweetStr = frontTweet + '\n' + backTweet
    if len(tweetStr) <= 140: break
print tweetStr
