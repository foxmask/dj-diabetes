# coding: utf-8
from dj_diabetes.models import HatModel


class Foods(HatModel):

    """
        Foods
    """
    class Meta:
        verbose_name = 'Foods'
        verbose_name_plural = 'Foods'

    def __str__(self):
        return "%s" % self.title
