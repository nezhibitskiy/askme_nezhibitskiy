from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def answer(request):
    return render(request, 'answer.html', {})

def login(request):
    return render(request, 'login.html', {})
