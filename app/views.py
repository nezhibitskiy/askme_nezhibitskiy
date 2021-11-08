from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.

new_questions = [
    {
        "title": f"Title {i}",
        "text": f"This is text for {i} question"
    } for i in range(50)
]

# def pagination():

def index(request):
    paginator = Paginator(new_questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'index.html', {'questions': content})

hot_questions = [
    {
        "title": f"Title {i}",
        "text": f"This is text for {i} hot question"
    } for i in range(100)
]

def hot(request):
    paginator = Paginator(hot_questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'hot.html', {'questions': content})

def question(request):
    return render(request, 'question.html', {})

def ask(request):
    return render(request, 'ask.html', {})

def singup(request):
    return render(request, 'singup.html', {})

# tags = ['perl', 'Python', 'TechnoPark', 'MySQL', 'django', 'Mail.ru', 'Chromium', 'FireFox']

# tag = [
#     {
#         "title": f"{tags[i]}"
#     } for i in range(tags.count)
# ]

<<<<<<< HEAD
def tag(request):
    # page = request.GET.get('page')    
    paginator = Paginator(new_questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'tags.html', {'questions': content})
=======
# def tag(request):
#     page = request.GET.get('page')
#     return render(request, 'tag.html', {})
>>>>>>> dataBase

def login(request):
    return render(request, 'login.html', {})
