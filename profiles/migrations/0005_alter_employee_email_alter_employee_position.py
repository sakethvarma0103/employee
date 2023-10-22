# Generated by Django 4.2.3 on 2023-10-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(default='', max_length=100),
        ),
    ]
