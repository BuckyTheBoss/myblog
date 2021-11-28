from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_pictures/', null=True, blank=True)
    author = models.CharField(max_length=60)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()


class Comment(models.Model):
    author = models.CharField(max_length=60)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

