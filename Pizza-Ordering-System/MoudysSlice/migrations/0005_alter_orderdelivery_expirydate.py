# Generated by Django 5.0.1 on 2024-02-22 09:55

import MoudysSlice.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoudysSlice', '0004_remove_pizza_spicychicken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdelivery',
            name='expirydate',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^(0[1-9]|1[0-2])\\/\\d{2}$', message='Enter a valid expiry date in MM/YY format.'), MoudysSlice.models.validate_card_expiry_date]),
        ),
    ]
