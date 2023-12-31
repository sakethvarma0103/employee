# Generated by Django 4.2.3 on 2023-10-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('image_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, default='')),
                ('age', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
