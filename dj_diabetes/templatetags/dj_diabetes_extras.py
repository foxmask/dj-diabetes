# -*- coding: utf-8 -*-
from dj_diabetes.models import Preferences

from django import template

register = template.Library()


@register.filter
def which_value(value, what):
    return Preferences.objects.get(value=value, key=what).title
