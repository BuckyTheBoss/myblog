from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_pictures/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    categories = models.ManyToManyField('Category')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.owner} {self.likes}'

    def get_absolute_url(self):
        return reverse('view_post', kwargs={'pk': self.id})

class Comment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    phone_number = PhoneNumberField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('view_post', kwargs={'pk': self.post.id})


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name