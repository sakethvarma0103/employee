from django.utils import timezone
from django.db import models
from django.utils.text import slugify
from django import forms
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import os

class Employee(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/')
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    age = models.IntegerField(default=0)
    email = models.EmailField(default='')
    position = models.CharField(max_length=100, default='')
    designation = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=20, default='')
    username = models.CharField(max_length=50, default='')

    def save(self, *args, **kwargs):
        # Set slug from email
        k = str(self.email).index("@")
        x = str(self.email)[:k]
        self.username = self.email
        self.slug = slugify(x)
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image)
            width, height = img.size

            if width != height:
                min_size = min(width, height)
                left = (width - min_size) / 2
                top = (height - min_size) / 2
                right = (width + min_size) / 2
                bottom = (height + min_size) / 2

                img = img.crop((left, top, right, bottom))

            img_format = img.format if img.format else 'JPEG'
            file_name, file_extension = os.path.splitext(self.image.name)
            if not file_extension:
                file_extension = '.jpg'
            final_file_name = f"{file_name}{file_extension}"

            # Save the cropped image back to the file field
            buffer = BytesIO()
            img.save(fp=buffer, format=img_format)
            self.image.save(final_file_name, ContentFile(buffer.getvalue()), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

class Search(models.Model):
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=100,default='')
    designation=models.CharField(max_length=100,default='')

class Tasks(models.Model):
    email=models.EmailField(default='')
    name=models.CharField(max_length=50)
    deadline=models.DateField(default=timezone.datetime.now)
    assigned=models.BooleanField(default=False)
    review=models.BooleanField(default=False)