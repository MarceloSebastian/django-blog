from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='default.png')

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.creator}\'s post'

