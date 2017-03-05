from twython import Twython
import random

tweets = list()
inputs = open('balaji.txt')

# Read in lines from balaji.txt
for line in inputs:
    if (line != '\n') and not(line.startswith('#')):
        tweets.append(line.strip())

# Sanity check tweet length
while(True):
    tweetStr = random.choice(tweets)
    if (len(tweetStr) <= 140):
        break

# Tweet the found string
apiKey = 'xxxxxxxxxxx'
apiSecret = 'xxxxxxxxxxx'
accessToken = 'xxxxxxxxxxx'
accessTokenSecret = 'xxxxxxxxxxx'
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
api.update_status(status=tweetStr)

# Comment this out when not testing
print ("Tweeted: ", tweetStr)
