from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('feedback/', views.feedback_view, name='feedback_view')
]
handler404 = 'university.views.custom_404_view'