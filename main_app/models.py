import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    user = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now(), editable=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user
