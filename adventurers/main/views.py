from django.shortcuts import render, redirect
from .models import Task, Story
from .forms import TaskForm
from django.views.generic.list import ListView

def index(request):
    tasks = Task.objects.order_by('-id')[:10]
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def saga_story(request):
    story = Story.objects.order_by('-id')
    return render(request, 'main/saga_story.html', {'title': 'История саги', 'story': story})


def about(request):
    story = Story.objects.order_by('-id')
    return render(request, 'main/about.html', {'title': 'История саги', 'story': story})


def tvorchestvo(request):
    return render(request, 'main/tvorchestvo.html')



def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была не верной'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)



def book_Of_The_Dead(request):
    return render(request, 'main/book_Of_The_Dead.html')


