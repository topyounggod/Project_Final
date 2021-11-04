
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/savestar/', views.savestar, name='savestar'),
]
