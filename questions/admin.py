from django.contrib import admin

from questions.models import Answer, Profile, Question, Status, Tag

# Register your models here.

admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Status)
admin.site.register(Tag)