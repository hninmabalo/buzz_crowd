from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Post, Profile


# Create your views here.
def index(request):

  # user_object = User.objects.get(username=request.user.username)
  # user_profile = Profile.objects.get(user=user_object)

  posts = list(Post.objects.all())

  return render(request, 'index.html', { 'posts': posts })

def about(request):
  return render(request, 'about.html')

def create_post(request):
  
  if request.method == 'POST':
    user = request.user.username
    image = request.FILES.get('image_upload')
    content = request.POST['content']

    new_post = Post.objects.create(user=user, image=image, content=content)
    new_post.save()

    return  HttpResponseRedirect('/')
  else:
    return  HttpResponseRedirect('/')

def profile(request, pk):
  profiles = list(Profile.objects.all())
  return render(request, 'profile.html', { 'profiles': profiles })
