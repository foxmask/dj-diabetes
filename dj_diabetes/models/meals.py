# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


class Meals(models.Model):

    """
        Meals
    """
    user = models.ForeignKey(User)
    food = models.TextField()
    breakfast_lunch_diner = models.CharField(max_length=2)
    date_meals = models.DateField(null=True)
    hour_meals = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'

    def __str__(self):
        return "%s (date: %s)" % (self.food, self.date_meals)
