from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog_app/index.html'
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog_app/create.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog_app/edit.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog_app/delete.html'
    success_url = reverse_lazy('post-list')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/detail.html'
    context_object_name = 'post'


def about(request):
    return render(request, 'blog_app/about.html')

def services(request):
    return render(request, 'blog_app/services.html')

def contact(request):
    return render(request, 'blog_app/contact.html')

