from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return '%s' % self.title
