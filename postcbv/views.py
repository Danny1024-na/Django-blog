from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView , DeleteView , UpdateView
from .models import Post

class postList(ListView):
    model = Post 

class PostDetails(DetailView):
    model = Post 

class postCreate(CreateView):
    model = Post
    fields =['title','image','content']
    success_url = '/blog/'

class postEdit(UpdateView):
    model = Post
    fields =['title','image','content']
    success_url = '/blog/'

class postDelete(DeleteView):
    model = Post
    success_url = '/blog/'
