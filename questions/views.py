from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import path, reverse
from django.contrib import auth
from django.contrib.auth.models import User
from questions.models import Question
from questions.forms import LoginForm, RegisterForm
# Create your views here.

def index(request):
    paginator = Paginator(Question.objects.new_questions(), 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'index.html', {'questions': content})

def hot(request):
    paginator = Paginator(Question.objects.hot_questions(), 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'hot.html', {'questions': content})

def question(request):
    return render(request, 'question.html', {})

@login_required(login_url='login')
def ask(request):
    return render(request, 'ask.html', {})

def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('next'))

def singup(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            cdata = form.cleaned_data
            user = User.objects.create_user(
                cdata['nickname'],
                cdata['email'],
                cdata['password']
            )
            user.save()
            print(cdata['nickname'], cdata['email'], cdata['password'])
            return redirect(request.GET.get('next'))
    else:
        form = RegisterForm()
    return render(request, 'singup.html', {'form': form})

def tag(request, **kwargs):
    chosen_tag = kwargs['tag']
    paginator = Paginator(Question.objects.get_tag(chosen_tag), 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'tags.html', {'questions': content, 'tag' : chosen_tag})


def login(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            cdata = form.cleaned_data
            user = auth.authenticate(
                username=cdata['username'],
                password=cdata['password']
            )
            if user is not None:
                auth.login(request, user)
                return redirect(request.GET.get('next'))
            form.add_error('username', "Wrong username or password")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
