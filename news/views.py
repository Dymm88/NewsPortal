from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Author, Post, Category
from .filters import PostFilter


class PostsList(ListView):
    model = Post
    ordering = 'date_create'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


class PostsSearch(ListView):
    model = Post
    ordering = 'date_create'
    template_name = 'search.html'
    context_object_name = 'search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'create.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'create.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post_list')
