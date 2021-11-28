from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_pictures/', null=True, blank=True)
    author = models.CharField(max_length=60)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
