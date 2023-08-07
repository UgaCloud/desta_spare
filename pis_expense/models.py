# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class ExtraExpense(models.Model):
    expense_type = models.CharField(max_length=100)
    amount=models.CharField(max_length=100, null=True, blank=True)
    description=models.CharField(max_length=100, null=True, blank=True)
    date=models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.amount