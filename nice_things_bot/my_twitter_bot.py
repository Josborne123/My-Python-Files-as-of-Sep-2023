import tweepy
import time
import random

CONSUMER_KEY = '1GRYKCnQgCgvqnihaNHpkx2jC'
CONSUMER_SECRET = 'kb1pfXY26NKWgXnUcu4kyctViILeX4pgxHNBKdKPGiuhkOBPOc'
ACCESS_KEY = '1282025013344903168-dgB9UyaJjV4Xf6AKjqIb81muNSWAHl'
ACCESS_SECRET = '9j8ZVNFqm6ZCt4E1XmhdztsGiaUhECdKj3EHsK5sWhNIY'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

nice_phrases_list = [' Have a nice day ', ' I hope you have a great year ', ' I hope you achieve all of your dreams ']
nice_phrases = random.choice(nice_phrases_list)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():
	print('finding and replying to tweets...')

	last_seen_id = retrieve_last_seen_id(FILE_NAME)
	mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

	for mention in reversed(mentions):
		print(str(mention.id) + ' - ' + mention.full_text)
		last_seen_id = mention.id
		store_last_seen_id(last_seen_id, FILE_NAME)
		
		if '' in mention.full_text.lower():
			print('responding ---- responding ---- responding')
			api.update_status('@' + mention.user.screen_name + nice_phrases, mention.id)


while True:
	reply_to_tweets()
	time.sleep(15)