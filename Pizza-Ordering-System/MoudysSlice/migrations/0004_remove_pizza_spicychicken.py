# Generated by Django 5.0.1 on 2024-02-13 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MoudysSlice', '0003_rename_jalapeños_pizza_jalapeños_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='Spicychicken',
        ),
    ]