from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PostModelForm
from .models import Post, Comment
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'


class PostCreateView(CreateView):
    form_class = PostModelForm
    success_url = reverse_lazy('homepage')


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostModelForm


class PostDetailView(DetailView):
    model = Post


class CommentCreateView(CreateView):
    # Either
    model = Comment
    fields = '__all__'
    # Or
    # form_class =
    # success_url = reverse_lazy('', kwargs={'pk':})

    def get_success_url(self):
        return reverse_lazy('view_post', kwargs={'pk': self.object.post.id})