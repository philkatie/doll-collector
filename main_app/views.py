from django.shortcuts import render
from django.http import HttpResponse
from .models import Doll

# Create your views here.

def home(request):
    return HttpResponse('<h1>Welcome to the dollhouse!</h1>')

def about(request):
    return render(request, 'about.html')

def dolls_index(request):
    dolls = Doll.objects.all()
    return render(request, 'dolls/index.html', { 'dolls': dolls }) 