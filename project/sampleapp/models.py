# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.
class Sampletbl(models.Model):
    col1 = models.CharField(max_length=100)
    col2 = models.TextField(null=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+". " + self.col1 + "--" + self.col2