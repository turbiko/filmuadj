from django.contrib import admin
from django.urls import path, include
from .views import announcement, announcements
urlpatterns = [
    path('/<str:pk>/', announcement),
    path('', announcements),
]

