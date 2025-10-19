from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('Главная страница университета')

def student_detail(request, student_id):
    return HttpResponse(f'Страница студента с ID {student_id}')
