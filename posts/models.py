from email.policy import default
from django.db import models
from accounts.models import Profile

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    due = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

