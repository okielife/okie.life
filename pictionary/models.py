from django.db import models


class WordModel(models.Model):
    word = models.CharField(max_length=100)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
