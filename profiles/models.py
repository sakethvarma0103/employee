from django.utils import timezone
from django.db import models
from django.utils.text import slugify
from django import forms
from django.contrib.auth.models import User

class Employee(models.Model):
    name=models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/')
    slug = models.SlugField(default="", blank=True,null=False, db_index=True)
    age=models.IntegerField(default=0)
    email=models.EmailField(default='')
    position=models.CharField(max_length=100,default='')
    designation=models.CharField(max_length=100,default='')
    phone_number = models.CharField(max_length=20,default='')
    username=models.CharField(max_length=50,default='')

    def save(self, *args, **kwargs):
        self.slug=slugify(self.username)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.name}"


class Search(models.Model):
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=100,default='')
    designation=models.CharField(max_length=100,default='')