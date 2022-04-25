from django.db import models
from django.urls import reverse

# Create your models here.

# class Doll:
#     def __init__(self, name, haunted, description, age):
#         self.name = name
#         self.haunted = haunted
#         self.description = description
#         self.age = age

# dolls = [
#     Doll('Amaya', True, 'desperate to take over your life', 15),
#     Doll('Persephone', False, 'surprisingly not haunted! but do NOT feed her pomegranite', 1745),
#     Doll('Chucky', True, 'the original Chucky doll! do not get too close to it', 34),
#     Doll('Mary Lou', True, 'when my grandma died she became a doll!', 97)
# ]

TYPES = (
    ('I', 'Informational'),
    ('S', 'Social'),
    ('E', 'Exorcism Attempt')    
)

class Doll(models.Model):
    name = models.CharField(max_length=100)
    haunted = models.BooleanField()
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('detail', kwargs={'doll_id': self.id})

class Seance(models.Model):
    date = models.DateField('seance date')
    type = models.CharField(
        max_length=1,
        choices=TYPES,
        default=TYPES[0][0]
    )

    doll = models.ForeignKey(Doll, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} on {self.date}"