from django.http.response import  HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.detail import DetailView
from .models import Post, Category, Profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User






# Define the home view
def home(request):
  return render(request, 'home.html')

@login_required
def posts_index(request):
  posts = Post.objects.all()
  
  return render(request, 'posts/index.html', { 'posts': posts })

@login_required
def profile(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'posts/profile.html', { 'posts': posts })

@login_required
def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    user_form = UserForm()
    return render(
        request, 
        'posts/detail.html', { 
            'post': post,
            'user_form': user_form,
        })

def get_context_data(self, *args, **kwargs):
    context=super(posts_detail, self).get_context_data
    stuff=get_object_or_404(Post, id=self.kwargs['post_id'])
    total_likes=stuff.total_likes()
    context['total_likes']=total_likes
    return context


def add_category(request, post_id):
    form = UserForm(request.POST)
    if form.is_valid():
        new_category = form.save(commit=False)
        new_category.post_id = post_id
        new_category.save()
    return redirect('detail', post_id=post_id)



def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('profile_create')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def LikeView(request, post_id):
    post= get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return redirect('index')

def profile_detail(request, pk):
  profile = Profile.objects.get(id=pk)
  user = profile.user.id
  # post = Post.objects.get(id__in=user.post.all().values_list('id'))
  post = Post.objects.filter(user=pk)
  
  return render(
    request, 
    'registration/user_profile.html', {
      'profile' : profile,
      'post' : post,
    })


class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'content', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user  # form.instance is the cat
    return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  fields = '__all__'

class PostDelete(LoginRequiredMixin, DeleteView):
  model = Post
  success_url = '/posts/'

class ProfileCreate(CreateView):
  model = Profile
  fields = ['name', 'avatar', 'bio']

  def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(UpdateView):
  model = Profile
  fields = ['name', 'avatar', 'bio']



