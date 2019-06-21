# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from tweetconsumer.models import Tweet
from tweetconsumer.utils import clean_tweet_obj, query_json


class TestUtilMethods(TestCase):
    def setUp(self):
        self.unmodded_tweet_obj = {
            "entities": {
                "hashtags": [
                    { "text": "cheese", "indicies": [1, 2]}
                ]
            },
            "user": {
                "screen_name": "uglyobj",
                "random_info": "random_info"
            },
            "retweeted_status": {
                "entities": {
                    "hashtags": [
                        { "text": "cheese", "indicies": [1, 2]}
                    ]
                },
                "user": {
                    "screen_name": "uglyobj",
                    "random_info": "random_info"
                },
                "retweeted_status"
                "text": "another test because tests are fun",
            },
            "text": "another test because tests are fun",
        }
        tweet_obj_1 = {
            "hashtags": [
                "photography"
            ],
            "user": "travelworlddddd",
            "text": "test dusk at Praia Dona Ana\n#travel #photography #nature #travelphotography #love #photooftheday "
                    "#instagood #travelgram… https://t.co/AEZVRMj0xF",
        }
        tweet_obj_2 = {
            "hashtags": [
                "funny"
            ],
            "user": "crazygoose",
            "text": "another test because tests are fun",
        }
        tweet_obj_3 = {
            "hashtags": [
                "nope"
            ],
            "user": "bad",
            "text": "kasbdkasbkdasdbaksdbjkasd",
        }

        Tweet.objects.create(name=tweet_obj_1["user"], tweet=tweet_obj_1)
        Tweet.objects.create(name=tweet_obj_2["user"], tweet=tweet_obj_2)
        Tweet.objects.create(name=tweet_obj_3["user"], tweet=tweet_obj_3)


    def test_clean_tweet_obj(self):
        expected = {
            "hashtags": ["cheese"],
            "user": "uglyobj",
            "text": "another test because tests are fun",
        }
        self.assertEquals(clean_tweet_obj(self.unmodded_tweet_obj), expected)

    def test_query_json(self):
        self.assertEqual(len(query_json("hashtags", "funny")), 1)
        self.assertEqual(len(query_json("user", "travelworlddddd")), 1)
        self.assertEqual(len(query_json("text", "test")), 2)


