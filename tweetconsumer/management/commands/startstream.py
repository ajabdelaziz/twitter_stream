import json

from django.core.management.base import BaseCommand
from django.conf import settings

from tweetconsumer.models import Tweet
from tweetconsumer.utils import clean_tweet_obj


class Command(BaseCommand):

    help = """
        uses tweepy to start real time never ending stream for twitter
    """

    def handle(self, *args, **options):
        import tweepy

        auth = tweepy.OAuthHandler(settings.CONSUMER_TOKEN, settings.CONSUMER_SECRET)
        auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
        try:
            auth.get_authorization_url()
        except tweepy.TweepError:
            print('Error! Failed to get request token.')

        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        class MyStreamListener(tweepy.StreamListener):

            def on_data(self, data):
                jdata = json.loads(data)
                # first check for hashtags and if its the hashtags we want
                wanted_hashtags = [
                    hashtag['text']
                    for hashtag in jdata['entities']['hashtags']
                    if hashtag['text'] in ["funny", "tech", "photography"]
                ]
                if len(wanted_hashtags):
                    mod_copy = clean_tweet_obj(jdata)
                    # save if all goes well
                    Tweet.objects.create(name=mod_copy['user'], tweet=mod_copy)
                    print("tweet saved")
                return True

        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener, timeout=60)
        myStream.filter(track=["photography", "tech", "funny"])

        running = True
        while running:
            if not myStream.running:
                running = False
