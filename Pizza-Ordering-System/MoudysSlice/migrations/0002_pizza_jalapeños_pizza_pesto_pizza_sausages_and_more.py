# Generated by Django 5.0.1 on 2024-02-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoudysSlice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='jalapeños',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pizza',
            name='pesto',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pizza',
            name='sausages',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pizza',
            name='spicychicken',
            field=models.BooleanField(default=False),
        ),
    ]
