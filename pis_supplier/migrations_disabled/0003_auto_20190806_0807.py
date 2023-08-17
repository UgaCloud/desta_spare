# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-08-06 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pis_supplier', '0002_auto_20190801_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplierstatement',
            name='payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='supplierstatement',
            name='supplier_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True),
        ),
    ]
