from django.shortcuts import render
from django.http import HttpResponse # если текст страницы прописывать ниже, без файлов штмл

def index (request):
    return render(request, 'index.html')

def about (request):
    return render(request, 'about.html')
