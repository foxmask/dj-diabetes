# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Glucoses(models.Model):

    """
        Glucoses
    """
    user = models.ForeignKey(User)
    moment = models.IntegerField(null=True)
    glucose = models.DecimalField(max_digits=5, decimal_places=2)
    insulin = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    comment = models.TextField()
    date_glucose = models.DateField()
    hour_glucose = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Glucose'
        verbose_name_plural = 'Glucoses'

    def show(self):
        return "Glucoses %s %s %s %s %s %s" % (self.user_id, self.moment,
                                               self.glucose, self.insulin,
                                               self.date_glucose,
                                               self.created, self.modified)

    def __str__(self):
        return "Glucose: %s Insulin: %s (date: %s)" % (
                                                self.glucose,
                                                self.insulin,
                                                self.date_glucose)
