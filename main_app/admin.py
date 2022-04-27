from django.contrib import admin
from .models import Doll, Seance, Talisman, Photo

# Register your models here.
admin.site.register(Doll)
admin.site.register(Seance)
admin.site.register(Talisman)
admin.site.register(Photo)