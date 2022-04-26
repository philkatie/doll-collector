from django.db import models
from django.urls import reverse
from datetime import date


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

HAUNTS = (
	('True', True),
	('False', False)
)

class Talisman(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('talismans_detail', kwargs={'pk': self.id})

class Doll(models.Model):
    name = models.CharField(max_length=100)
    haunted = models.CharField(
		max_length=5,
		choices=HAUNTS,
		default=HAUNTS[0]
	)
    # haunted = models.BooleanField()
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    talismans = models.ManyToManyField(Talisman)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('detail', kwargs={'doll_id': self.id})
        
    def seance_today(self):
        return self.seance_set.filter(date=date.today()).count() >= 1


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
    
    class Meta:
        ordering = ['-date']

