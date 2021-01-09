from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    handle = models.CharField(max_length=100, unique=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField()
    date_joined = models.DateTimeField(default=datetime.now, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username} Profile'
