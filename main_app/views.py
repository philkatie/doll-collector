from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Doll, Talisman, Photo
from .forms import SeanceForm

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'catcollectorphilkatie'

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
    talismans_doll_doesnt_have = Talisman.objects.exclude(id__in = doll.talismans.all().values_list('id'))
    seance_form = SeanceForm()
    return render(request, 'dolls/detail.html', { 
        'doll': doll, 'seance_form': seance_form, 'talismans': talismans_doll_doesnt_have 
    }) 

def add_seance(request, doll_id):
    form = SeanceForm(request.POST)
    if form.is_valid():
        new_seance = form.save(commit=False)
        new_seance.doll_id = doll_id
        new_seance.save()
    return redirect('detail', doll_id=doll_id)

def add_photo(request, doll_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, doll_id=doll_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', doll_id=doll_id)

def assoc_talisman(request, doll_id, talisman_id):
    Doll.objects.get(id=doll_id).talismans.add(talisman_id)
    return redirect('detail', doll_id=doll_id)

def unassoc_talisman(request, doll_id, talisman_id):
    Doll.objects.get(id=doll_id).talismans.remove(talisman_id)
    return redirect('detail', doll_id=doll_id)

class TalismanList(ListView):
    model = Talisman

class TalismanDetail(DetailView):
    model = Talisman

class TalismanCreate(CreateView):
    model = Talisman
    fields = '__all__'

class TalismanUpdate(UpdateView):
    model = Talisman
    fields = ['name', 'color']

class TalismanDelete(DeleteView):
    model = Talisman
    success_url = '/talismans/'