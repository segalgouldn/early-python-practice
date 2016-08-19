from twython import Twython

import time, random, nltk

def helpMeWords():

	appKey = "INSERT_APP_KEY"
	
	appSecret = "INSERT_APP_SECRET"

	tokenKey =  "INSERT_TOKEN_KEY"

	tokenSecret = "INSERT_TOKEN_SECRET"

	twitter = Twython(appKey, appSecret, tokenKey, tokenSecret)

	f = open("words.txt")
	words = f.read().split()
	f.close()
	tags = nltk.pos_tag(words)

	for i in range(1000000):
		word = random.choice(tags)
		if word[1] == "NN" or word[1] == "NNS":
			twitter.update_status(status = "Help me, " + word[0])
		elif word[1] == "VB":
			twitter.update_status(status = "Help me " + word[0])
		words.remove(word[0])
		time.sleep(300)

helpMeWords()
