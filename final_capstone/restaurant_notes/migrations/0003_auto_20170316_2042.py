# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_notes', '0002_auto_20170316_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantnote',
            name='note_text',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
