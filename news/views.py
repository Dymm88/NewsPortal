from django.views.generic import ListView, DetailView
from .models import Author, Post, Category


class PostsList(ListView):
    model = Post
    ordering = 'author'
    template_name = 'news.html'
    context_object_name = 'news'


class PostsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
