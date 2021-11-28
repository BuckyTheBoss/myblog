from django import forms
from .models import Post

# class PostForm(forms.Form):
#     title = forms.CharField(max_length=200)
#     content = forms.TextField()
#     image = forms.ImageField(upload_to='post_pictures/')
#     author = forms.CharField(max_length=60)
#     timestamp = forms.DateTimeField(auto_now_add=True)


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['timestamp', 'likes']
