from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Post, Profile


# Create your views here.
def index(request):

    # user_object = User.objects.get(username=request.user.username)
    # user_profile = Profile.objects.get(user=user_object)

    posts = list(Post.objects.all())

    return render(request, 'index.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')


def create_post(request):

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        content = request.POST['content']

        new_post = Post.objects.create(user=user, image=image, content=content)
        new_post.save()

        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def profile(request, pk):
    profiles = list(Profile.objects.all())
    return render(request, 'profile.html', {'profiles': profiles})


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Exists')
                return HttpResponseRedirect('/signup/')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Exists')
                return HttpResponseRedirect('/signup/')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return HttpResponseRedirect('/login/')
        else:
            messages.info(request, 'Password Does Not Match')
            return HttpResponseRedirect('/signup/')
    else:
        return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    logout(request)
    return HttpResponseRedirect('/')
