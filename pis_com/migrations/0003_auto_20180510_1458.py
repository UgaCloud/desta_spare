# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-10 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pis_com', '0002_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('shop', 'Shop'), ('company', 'Company'), ('individual', 'Individual')], default='shop', max_length=100),
        ),
    ]