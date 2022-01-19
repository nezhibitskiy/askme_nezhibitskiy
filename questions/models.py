from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey
from django.shortcuts import reverse

from datetime import date

from django.contrib.auth.models import User
# from questions.managers.managers import QuestionManager

class QuestionManager(models.Manager):
    def new_questions(self):
        return self.order_by('-created_at')
    def hot_questions(self):
        return self.order_by('rating')
    def get_tag(self, tag):
        return self.filter(tags__title=tag).order_by('rating')


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    # avatar = models.ImageField(upload_to='avatars', default='default.jpg')

    # def __str__(self):
        # return self.user

class Question(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    likes = GenericRelation('Like')
    rating = models.IntegerField(default=0)
    tags = models.ManyToManyField(to='Tag', related_name='questions')
    
    created_at = models.DateTimeField(auto_now_add=True)

    objects = QuestionManager()

    def __str__(self):
        return self.title

class Like(models.Model):
    VALUES = (
        ('UP', 1),
        ('DOWN', -1),
    )
    value = models.SmallIntegerField(choices=VALUES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class Tag(models.Model):
    title = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tag", kwargs={'tag': self.title})

class Answer(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(default=(19990101))
    author = models.ForeignKey(Profile, default=0, on_delete=models.CASCADE)
    question = ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text
    def get_user(self):
        return Profile.objects.get(user=self.author)