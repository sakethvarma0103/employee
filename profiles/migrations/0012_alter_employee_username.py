# Generated by Django 4.2.3 on 2023-10-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_alter_employee_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
