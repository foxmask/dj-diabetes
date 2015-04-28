# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

from dj_diabetes.models import HatModel


class Sports(HatModel):

    """
        Sports
    """
    class Meta:
        verbose_name = 'Sports'
        verbose_name_plural = 'Sports'


@python_2_unicode_compatible
class Exercises(models.Model):

    """
        Exercises
    """
    user = models.ForeignKey(User)
    sports = models.ForeignKey(Sports)
    comment = models.TextField()
    duration = models.FloatField()
    date_exercise = models.DateField(null=True)
    hour_exercise = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def show(self):
        return "Exercises %s %s %s %s %s" % (self.user_id, self.sports,
                                             self.comment, self.created,
                                             self.modified)

    def __str__(self):
        return "%s (duration: %s)" % (self.sports, self.duration)
