from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=150,null=True)
    active = models.BooleanField()