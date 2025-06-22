from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/', views.course_list, name='course_list'),
    path('learning/<int:topic_id>/', views.learning, name='learning'),
]