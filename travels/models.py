from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from posts.models import Post

# Create your models here.

class Travel(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    region = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True, default=1)
    short_content = models.CharField(max_length=50)
    long_content = models.CharField(max_length=100)
    hashtag = models.CharField(max_length=200, default=1)
    image = models.ImageField(upload_to='travels', null=True)
    image_second = models.ImageField(upload_to='travels', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    liked_users = models.ManyToManyField(User, related_name='liked_travels')
    coordinates = models.CharField(max_length=100, default="33.361365, 126.529669")

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


