from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Doll:
    def __init__(self, name, haunted, description, age):
        self.name = name
        self.haunted = haunted
        self.description = description
        self.age = age

dolls = [
    Doll('Amaya', True, 'desperate to take over your life', 15),
    Doll('Persephone', False, 'surprisingly not haunted! but do NOT feed her pomegranite', 1745),
    Doll('Chucky', True, 'the original Chucky doll! do not get too close to it', 34),
    Doll('Mary Lou', True, 'when my grandma died she became a doll!', 97)
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to the dollhouse!</h1>')

def about(request):
    return render(request, 'about.html') 
    return render(request, 'about.html')

def dolls_index(request):
    return render(request, 'dolls/index.html', { 'dolls': dolls }) 