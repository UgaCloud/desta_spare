# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-07-31 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier', to='pis_supplier.Supplier')),
            ],
        ),
    ]