from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import login
from .form import LoginForm
from .form import RegistrationForm 
from .form import FeedbackForm

STUDENTS_DATA = {
    1: {
        'info': 'Иван Петров',
        'faculty': 'Кибербезопасность',
        'status': 'Активный',
        'year': 3
    },
    2: {
        'info': 'Мария Сидорова', 
        'faculty': 'Информатика',
        'status': 'Активный',
        'year': 2
    },
    3: {
        'info': 'Алексей Козлов',
        'faculty': 'Программная инженерия', 
        'status': 'Выпускник',
        'year': 5
    }
}

COURSES_DATA = {
    'python-basics': {
        'name': 'Основы программирования на Python',
        'duration': 36,
        'description': 'Базовый курс по программированию на языке Python для начинающих.',
        'instructor': 'Доцент Петров И.С.',
        'level': 'Начальный'
    },
    'web-security': {
        'name': 'Веб-безопасность',
        'duration': 48,
        'description': 'Курс по защите веб-приложений от современных угроз.',
        'instructor': 'Профессор Сидоров А.В.',
        'level': 'Продвинутый'
    },
    'network-defense': {
        'name': 'Защита сетей',
        'duration': 42,
        'description': 'Изучение методов и технологий защиты компьютерных сетей.',
        'instructor': 'Доцент Козлова М.П.',
        'level': 'Средний'
    }
}

def home(request):
    return render(request, 'home.html', status=200)

def student_detail(request, student_id):
    if student_id in STUDENTS_DATA:
        student_data = STUDENTS_DATA[student_id]
        return render(request, 'student_detail.html', {
            'student_id': student_id,
            'student_info': student_data['info'],
            'faculty': student_data['faculty'],
            'status': student_data['status'],
            'year': student_data['year']
        })
    else:
        return render(request, '404.html', status=404)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def login_view(request):
    if request.method == 'POST': 
        form = LoginForm(request.POST) 
        if form.is_valid(): 
            user = form.get_user() 
            
            return render(request, 'success.html', { 
                'message': 'Вход выполнен успешно! Добро пожаловать в систему.',
                'title': 'Вход в систему'
            })
    else:
        form = LoginForm() 
    
    return render(request, 'login.html', { 
        'form': form, 
        'title': 'Вход в систему'
    })

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Данные уже валидны и очищены
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Создаем пользователя
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            return render(request, 'success.html', {
                'message': 'Регистрация прошла успешно! Теперь вы можете войти в систему.',
                'title': 'Регистрация успешна'
            })
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {
        'form': form,
        'title': 'Регистрация'
    })

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return render(request, 'success.html', {
                'message': 'Спасибо за ваш отзыв!',
                'title': 'Отзыв получен'
            })
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {
        'form': form,
        'title': 'Обратная связь'
    })
