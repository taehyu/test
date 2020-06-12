from django.db import models


class Card(models.Model):
    title = models.CharField()
    user = models.CharField()
    card = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']