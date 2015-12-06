# coding: utf-8
from django.db import models
from django.contrib.auth.models import User

from dj_diabetes.models import HatModel


class Sports(HatModel):

    """
        Sports
    """
    class Meta:
        verbose_name = 'Sports'
        verbose_name_plural = 'Sports'

    def show(self):
        return "%s" % self.title

    def __str__(self):
        return self.show()


class Exercises(models.Model):

    """
        Exercises
    """
    user = models.ForeignKey(User)
    sports = models.ForeignKey(Sports)
    comment = models.TextField()
    duration = models.FloatField()
    date_exercises = models.DateField(null=True)
    hour_exercises = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def show(self):
        return "%s (duration: %s)" % (self.sports, self.duration)

    def __str__(self):
        return self.show()
