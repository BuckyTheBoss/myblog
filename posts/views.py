from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PostModelForm
from .models import Post
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView


class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('homepage')


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostModelForm

