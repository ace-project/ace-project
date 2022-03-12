from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from posts.models import Post

# Create your models here.

class Travel(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    taste = models.CharField(max_length=100)
    short_content = models.CharField(max_length=50)
    long_content = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='travels', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    liked_users = models.ManyToManyField(User, related_name='liked_travels')

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE, null=True, related_name='travel_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='post_comments')

    def __str__(self):
        return f'{self.author} {self.travel} {self.post}'


