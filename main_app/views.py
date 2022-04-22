from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Doll

class DollCreate(CreateView):
    model = Doll
    fields = '__all__'

# Create your views here.

def home(request):
    return HttpResponse('<h1>Welcome to the dollhouse!</h1>')

def about(request):
    return render(request, 'about.html')

def dolls_index(request):
    dolls = Doll.objects.all()
    return render(request, 'dolls/index.html', { 'dolls': dolls }) 

def dolls_detail(request, doll_id):
    doll = Doll.objects.get(id=doll_id)
    return render(request, 'dolls/detail.html', { 'doll': doll }) 