# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField


class Tweet(models.Model):
    name = models.CharField(max_length=200)
    tweet = JSONField()

    def __str__(self):
        return self.name
