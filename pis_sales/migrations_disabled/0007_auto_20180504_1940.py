# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-04 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pis_sales', '0006_auto_20180427_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='retailer',
        ),
        migrations.AlterField(
            model_name='saleshistory',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_sales', to='pis_com.Customer'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]

