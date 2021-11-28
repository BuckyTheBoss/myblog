from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_pictures/', null=True, blank=True)
    author = models.CharField(max_length=60)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return f'{self.title} {self.author} {self.likes}'


class Comment(models.Model):
    author = models.CharField(max_length=60)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    phone_number = PhoneNumberField()


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name