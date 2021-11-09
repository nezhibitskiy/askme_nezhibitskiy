from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

from django.contrib.auth.models import User
from app.views import question

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    # avatar = models.ImageField(upload_to='avatars', default='default.jpg')

class Question(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    tags = models.ManyToManyField(to='Tag', related_name='questions')

class Status(models.Model):
    likes = models.IntegerField(default=0)

class Tag(models.Model):
    title = models.SlugField(unique=True)

class Answer(models.Model):
    text = models.TextField()
    question = ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
