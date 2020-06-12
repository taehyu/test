# class CardSerializer(serializers.ModelSerializer):
#   class Meta:
#      model = cards
#     fields = ("id", "number_of_cards")
# fields = ("id", "reply_id","comment_content", "comment_create_time", "post", "user")
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            # 'card',
        ]
