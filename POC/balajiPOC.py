import random

tweets = list()
inputs = open('balaji.txt')
for line in inputs:
    if (line != '\n') and not(line.startswith('#')):
        tweets.append(line.strip())
while(True):
    tweetStr = random.choice(tweets)
    if (len(tweetStr) <= 140):
        break
    
print tweetStr
