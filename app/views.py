from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import pytz
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now(pytz.timezone(
        'Europe/Moscow')).time().replace(microsecond=0)
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    template_name = 'app/list.html'
    work_files = os.listdir()
    print(work_files)
    return render(request, template_name, context= {'files': work_files})
