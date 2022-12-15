from django.shortcuts import render
from django.contrib.auth.models import User

from django.http import HttpResponse
from .models import Post, Profile

# Create your views here.
def index(request):
  posts = list(Post.objects.all())
  return render(request, 'index.html', { 'posts': posts })

def about(request):
  return render(request, 'about.html')

def profile(request, pk):
  profiles = list(Profile.objects.all())
  return render(request, 'profile.html', { 'profiles': profiles})