from django.contrib.auth.models import User
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'username', 'email']