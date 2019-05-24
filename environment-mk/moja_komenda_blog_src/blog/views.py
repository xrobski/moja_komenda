from django.shortcuts import render
from django.http import HttpResponse

posts =[
    {
        'author': 'Kamil Drukała',
        'title': 'Rozprułem się po raz 1',
        'content': 'Pamiętam to jak wczoraj..',
        'date_posted': 'Listopad 29, 2019'
    },
    {
        'author': 'Michał Chrząszcz',
        'title': 'Nigdy się nie rozprułem',
        'content': 'Pamiętam to jak wczoraj..',
        'date_posted': 'Listopad 28, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
