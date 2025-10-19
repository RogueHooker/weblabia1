from django.shortcuts import render
from django.http import HttpResponse, Http404

def home(request):
    return render(request, 'home.html', status=200)

def student_detail(request, student_id):
    if student_id < 1:
        return render(request, '404.html', status=404)
    return render(request, 'student_detail.html', {'student_id': student_id})

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
