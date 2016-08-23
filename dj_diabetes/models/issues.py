# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


class Issues(models.Model):

    """
        Issues asked from the user
    """
    user = models.ForeignKey(User)
    question = models.TextField()
    question_to = models.CharField(max_length=255)
    answer = models.TextField(null=True, blank=True)
    date_answer = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Issues'
        verbose_name_plural = 'Issues'

    def __str__(self):
        return "%s" % self.question
