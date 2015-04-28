# coding: utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Foods(models.Model):

    """
        Foods
    """
    title = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Foods'
        verbose_name_plural = 'Foods'

    def show(self):
        return "Foods %s %s %s" % (self.title, self.created, self.modified)

    def __str__(self):
        return "%s" % (self.title)
