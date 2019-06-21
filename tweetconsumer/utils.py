from copy import deepcopy
from tweetconsumer.models import Tweet


# consumes tweet object from tweepy and spits out a modified copy that's easier to work with
def clean_tweet_obj(orig_obj):
    mod_copy = deepcopy(orig_obj)
    mod_copy['hashtags'] = [
        hashtag['text']
        for hashtag in orig_obj['entities']['hashtags']
    ]
    # get rid of nested entities object
    del mod_copy['entities']

    # flatten user object and get rid of nested retweeted_status
    mod_copy['user'] = orig_obj['user']['screen_name']
    if mod_copy.get('retweeted_status', False):
        del mod_copy['retweeted_status']
    return mod_copy


def query_json(filter, q):
    where_filter = f"tweet->>'{filter}' ILIKE %s"
    params = f"%{q}%"
    return list(Tweet.objects.extra(where=[where_filter], params=[params]).values())
