#########################################################
#
# Instructions:
#
# create an empty file caled last_mined.txt
# in the same folder with the script and
# add a bogus value in the first line, between 300 and 1000
#
# manually run the script with python3 tweet-mine.py
#
# when it runs for the first time it will initialize with
# the seed value from the first line of last_mined.txt
#
# after that, it will constantly update the first line
# with the last recorded value in the wallet
#
# if there is no difference between the current amount
# in the wallet and the one in last_mined.txt it won't
# trigger a tweet.
#
# if there is a difference from the wallet value and
# the amount in last_mined.txt it will calculate
# the amount mined and it will trigger the tweet
#
###########################################################

import subprocess


p = subprocess.Popen('/usr/bin/21 status', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    if(b"Mined (all time)" in line):
        list_data = str.split(line.decode('utf-8'), ":");
        satoshis_list = str.split(list_data[1].strip(), " ");
        satoshis = satoshis_list[0]
        
        
    if(b"Hashrate" in line):
        list_data = str.split(line.decode('utf-8'), ":");
        hashrate_list = str.split(list_data[1].strip(), " ");
        hashrate = hashrate_list[0]      
        
        
retval = p.wait()

# checking the data in the last_mined.txt file
# and see if we have a difference

with open('last_mined.txt', 'r+') as f:
    last_record = f.readline()

if(last_record == satoshis):
    tweet = False
else:
    tweet = True
    satoshis_mined = int(satoshis) - int(last_record)
    tweetStr = "@FJasonSeibert is not my lawyer\nIn the last hour, I've mined " + str(satoshis_mined) + " Satoshis!\nTo date, I've mined " + str(satoshis) + " Satoshis!\nMy current hashrate is " + str(hashrate) + " GH/s!"

# update the last_mine value in the file

with open('last_mined.txt', 'w+') as f:
     f.write(str(satoshis))

if(tweet == True):
    # add the Tweet update function and comment the print(tweetStr) line
    # uncomment it if you want to see debugging output
    # keep the indentation, otherwise Python will complain

    #!/usr/bin/env python
    
    import sys
    from twython import Twython

    apiKey = 'xxxxxxxxxxx'
    apiSecret = 'xxxxxxxxxxx'
    accessToken = 'xxxxxxxxxxx'
    accessTokenSecret = 'xxxxxxxxxxx'
    api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
    api.update_status(status=tweetStr)
    print ("Tweeted: ", tweetStr)