from ast import Mod
from pyexpat import model
from django.db import models

# reverse modeling: python manage.py inspectdb > demo/models.py


class Question(models.Model):
    title = models.CharField(max_length=50, default='')
    pub_date = models.DateTimeField()
    contents = models.CharField(max_length=200)

# foreign key(one to many)


class School(models.Model):
    name = models.CharField(max_length=50)


class Collage(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

# foreign key(one to one, many to many)


class Location(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    collage = models.OneToOneField(
        Collage,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    adjoin = models.ManyToManyField("self")

# foreign key(many to many)


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    collage = models.ManyToManyField(Collage)
