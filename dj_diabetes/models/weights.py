# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


class Weights(models.Model):

    """
        Weight
    """
    user = models.ForeignKey(User)
    weight = models.FloatField()
    date_weights = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Weight'
        verbose_name_plural = 'Weights'

    def __str__(self):
        return "%s (date: %s)" % (self.weight, self.date_weights)
