# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-08 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pis_product', '0004_extraitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='extraitems',
            name='discount_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True),
        ),
    ]
