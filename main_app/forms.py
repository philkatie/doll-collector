from django.forms import ModelForm
from .models import Seance

class SeanceForm(ModelForm):
    class Meta:
        model = Seance
        fields = ['date', 'type']