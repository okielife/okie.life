from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import uuid


class Card(models.Model):
    character = models.CharField(max_length=100)
    static_image_path = models.CharField(max_length=200, default='images/logo.png')

    def __str__(self):
        return self.character


class CardInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular card instance")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.owner:
            return 'Card type %s; owned by %s' % (self.card.character, self.owner.get_username())
        else:
            return 'Card type %s; unowned' % self.card.character
