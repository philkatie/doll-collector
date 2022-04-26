from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Doll, Talisman
from .forms import SeanceForm

class DollCreate(CreateView):
    model = Doll
    fields = '__all__'

class DollUpdate(UpdateView):
    model = Doll
    fields = ['name', 'description', 'age']

class DollDelete(DeleteView):
    model = Doll
    success_url = '/dolls/'

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dolls_index(request):
    dolls = Doll.objects.all()
    return render(request, 'dolls/index.html', { 'dolls': dolls }) 

def dolls_detail(request, doll_id):
    doll = Doll.objects.get(id=doll_id)
    seance_form = SeanceForm()
    return render(request, 'dolls/detail.html', { 
        'doll': doll, 'seance_form': seance_form 
    }) 

def add_seance(request, doll_id):
    form = SeanceForm(request.POST)
    if form.is_valid():
        new_seance = form.save(commit=False)
        new_seance.doll_id = doll_id
        new_seance.save()
    return redirect('detail', doll_id=doll_id)

class TalismanList(ListView):
    model = Talisman

class TalismanDetail(DetailView):
    model = Talisman

class TalismanCreate(CreateView):
    model = Talisman
    fields = '__all__'

class TalismanDelete(DeleteView):
    model = Talisman
    success_url = '/talismans/'