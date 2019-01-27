import tweepy

'''
!!!user.name() should retrun testing
scrapes tweets runs statistics
cameron-chromiak
'''

# Consumer keys and access tokens, used for OAuth
consumer_key = 'SLlOSYDDqlvpIy4C4idFQwfTL'
consumer_secret = 'ReI1JoVs0swujvMW3RyoMmVZoc35h7ZuYU5SPTPvnrCA4sdUuT'
access_token = '1087755752763285504-AIpyDSITUSnGTIBwxZF8a8G5Pxj6EE'
access_token_secret = 'tHpLltK4btp196PT7Wr5rLAhk3IWhHi1yev2OTuGTkUhX'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)
target_user = 'realDonaldTrump'

tweets = api.user_timeline(target_user)
# Empty Array
tmp=[]

tweets_text = [tweet.text for tweet in tweets]
for j in tweets_text:
    tmp.append(j)

print(tmp)
