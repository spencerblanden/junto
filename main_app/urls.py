from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.posts_index, name='index'),
    path('posts/<int:post_id>/', views.posts_detail, name='detail'),

]