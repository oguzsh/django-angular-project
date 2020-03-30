from django.db import models


class Note(models.Model):
    noteTitle = models.CharField(max_length=70)


class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    notes = models.ManyToManyField(Note)
