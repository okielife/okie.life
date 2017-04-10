from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('blog:view_blog_category', args=[str(self.id)])


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    category = models.ForeignKey(Category, related_name="category")
    posted = models.DateField(db_index=True, auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(null=True)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('blog:view_blog_post', args=[str(self.id)])
