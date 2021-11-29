from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PostModelForm
from .models import Post, Comment
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
import random


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'


class PostCreateView(CreateView):
    model = Post
    form_class = PostModelForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.likes = random.randint(20, 40)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self,  request, *args, **kwargs):
        print(request.user)
        return super().get(request, *args, **kwargs)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostModelForm


class PostDetailView(DetailView):
    model = Post


class CommentCreateView(CreateView):
    # Either
    model = Comment
    fields = '__all__'
    template_name = 'posts/post_form.html'
    # Or
    # form_class =
    # success_url = reverse_lazy('', kwargs={'pk':})

    # def get_success_url(self):
    #     return reverse_lazy('view_post', kwargs={'pk': self.object.post.id})