from django.contrib import admin

from questions.models import Answer, Like, Profile, Question, Tag

# Register your models here.

admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(Like)