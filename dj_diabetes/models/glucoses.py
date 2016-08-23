# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


class Glucoses(models.Model):

    """
        Glucoses
    """
    user = models.ForeignKey(User)
    moment = models.IntegerField(null=True)
    glucose = models.DecimalField(max_digits=5, decimal_places=2)
    insulin = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    comment = models.TextField()
    date_glucoses = models.DateField()
    hour_glucoses = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Glucose'
        verbose_name_plural = 'Glucoses'

    def __str__(self):
        return "Glucose: %s Insulin: %s (date: %s)" % (
                                                self.glucose,
                                                self.insulin,
                                                self.date_glucoses)
