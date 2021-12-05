from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.

class new(models.Model):
    GENDER = (
    (None, 'Gender'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    )
    DIET = (
    (None, 'diet'),
    ('vegetarian', 'Vegetarian'),
    ('vegan', 'Vegan'),
    ('gluten-free', 'Gluten free'),
    ('alcohol-free', 'Alcohol Free'),
    )
    DISORDER = (
    (None, 'Disorder'),
    ('Binge-eating', 'Binge-eating'),
    ('Anorexia-nervosa', 'Anorexia nervosa'),
    )
    user = models.OneToOneField(User ,null = True, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, null=True)
    weight = models.FloatField(max_length=50, null=True)
    height = models.FloatField(max_length=20,null=True)
    age = models.IntegerField(null=True)
    gender1= models.CharField(max_length=50, choices=GENDER, verbose_name="gender", blank=True)
    diet=models.CharField(max_length=50, choices=DIET, verbose_name="diet", blank=True)
    disorder=models.CharField(max_length=50, choices=DISORDER, verbose_name="diet", blank=True)
    
    def __str__(self):
        return '{}'.format(self.fname)
