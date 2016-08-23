# coding: utf-8
from dj_diabetes.models import HatModel

from django.contrib.auth.models import User
from django.db import models


class ExaminationTypes(HatModel):

    """
        ExaminationTypes
    """
    class Meta:
        verbose_name = 'Examination Types'
        verbose_name_plural = 'Examination Types'


class Examinations(models.Model):

    """
        Examinations
    """
    user = models.ForeignKey(User)
    examination_types = models.ForeignKey(ExaminationTypes)
    comments = models.TextField()
    date_examinations = models.DateField()
    hour_examinations = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Examinations'
        verbose_name_plural = 'Examinations'

    def __str__(self):
        return "%s (date %s) (comment: %s)" % (
            self.examination_types,
            self.date_examinations,
            self.comments)


class ExaminationDetails(models.Model):

    """
        ExaminationDetails
    """
    examination = models.ForeignKey(Examinations)
    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=15, decimal_places=5)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Examination Details'
        verbose_name_plural = 'Examination Details'

    def __str__(self):
        return "%s" % self.title
