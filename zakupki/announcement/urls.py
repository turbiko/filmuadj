from django.contrib import admin
from django.urls import path, include
from .views import announcement_detail, announcements

app_name = 'announcement'

urlpatterns = [
    path('<str:pk>/', announcement_detail, name='announcement_detail'),
    path('', announcements, name='announcement_detail'),
]

