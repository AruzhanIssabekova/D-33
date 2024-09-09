# Generated by Django 5.0.6 on 2024-09-09 16:56

import localflavor.us.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='postal_code',
            field=localflavor.us.models.USPostalCodeField(blank=True, max_length=2, null=True),
        ),
    ]
