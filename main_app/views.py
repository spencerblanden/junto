from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Define the home view
def home(request):
  return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', { 'posts': posts })

def posts_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'posts/detail.html', { 'post': post })


class PostCreate(CreateView):
  model = Post
  fields = '__all__'

class PostUpdate(UpdateView):
  model = Post
  fields = '__all__'

class PostDelete(DeleteView):
  model = Post
  success_url = '/posts/'