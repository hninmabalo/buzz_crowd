
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
#profile models
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    nickname = models.CharField(max_length=50, blank=True, null=True)
    pronouns = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images', default='blank_profile.png')
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username 


#posts models that user can post content/images
class Post(models.Model):
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user



