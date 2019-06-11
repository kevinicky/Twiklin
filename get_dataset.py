import tweepy
import csv
from nltk.tokenize import word_tokenize

consumer_key = 'qwFexwZ95GXY1EVRWlxr3ZJnL'
consumer_key_secret = '5vJxUIh74oOIqckSacDWTJ7T2ANqTIhmUUpkmI8vcMZ0zmlWRJ'
access_token = '2285972083-8f4L3CCiSqoMNo6ivDJg4FaKEzIuRQTXDjEzZ5L'
access_token_secret = 'auHv2h6TLsxULyPU45GKskpPV8TRsEYnd5BHU2PoYrAQG'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('dataset.csv', 'a', newline = '')

csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q='#prabowo -filter:retweets', tweet_mode='extended').items(300):
    t = tweet.full_text
    print(tweet.full_text)
    csvWriter.writerow([tweet.full_text.encode('utf-8')])
    # csvWriter.writerow([tweet.full_text])

csvFile.close()
print()
print('success get tweets')
print('tweet saved to dataset.csv')