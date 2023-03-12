from django.shortcuts import render
from django.http import HttpResponse # если текст страницы прописывать ниже, без файлов штмл
from .models import Task
from.forms import TaskForm

def index(request):
    task = Task.objects.order_by('-id')
    return render(request, 'index.html', {'title': 'Главная страница', 'tasks': task})


def about(request):
    return render(request, 'about.html')


def create(request):
    form = TaskForm()
    context = {
        'form':form
    }
    return render(request, 'create.html')

