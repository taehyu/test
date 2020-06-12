from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers


class Card(models.Model):
    user = models.ForeignKey(User, related_name="post_user")
    # card = models.ForeignKey(Card, related_name='post_card")

