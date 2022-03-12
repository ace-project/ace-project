import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=100)
    mbti = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=50)
    introduce = models.CharField(max_length=100)
    image = models.ImageField(upload_to='accounts', null=True)

    def __str__(self):
        return f'{self.user}'