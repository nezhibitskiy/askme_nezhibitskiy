from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def answer(request):
    return render(request, 'answer.html', {})

def ask(request):
    return render(request, 'ask.html', {})

def singup(request):
    return render(request, 'singup.html', {})

def login(request):
    return render(request, 'login.html', {})
