# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantnote',
            name='restaurant_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]