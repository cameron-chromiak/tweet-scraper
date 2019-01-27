import tweepy

'''
!!!user.name() should retrun testing
scrapes tweets runs statistics
cameron-chromiak
'''

# Consumer keys and access tokens, used for OAuth
consumer_key = 'lHWHzGfCb6o03KtMRUHhvs3V6'
consumer_secret = 'WLDmi7wf7NEGFixQ9Y4aRtWQR9DuTdyO1FgudMlPqAd70KLE6W'
access_token = '1087755752763285504-tzVFaMkTIqeH5YnoDTv7t1eg4JeX1o'
access_token_secret = 'h5e6IY3Inr7tdC52NTCC0VP45OSolSNoAbJbF5ujEiizY'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

account_to_search = 'realDonaldTrump'

tweets_by_target = api.get_user(account_to_search)
print(tweets_by_target.followers_count)

hashtags = []
words = []
tweet_count = 0

for status in tweepy.Cursor(api.user_timeline, tweets_by_target).items(1):
    print(status)
    for ent in
