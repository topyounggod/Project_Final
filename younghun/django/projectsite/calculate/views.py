from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def calculate(request):
    return HttpResponse("calculate, calculate funtion!")
