# -*- coding: utf-8 -*-
from django import template
from dj_diabetes.models import Preferences

register = template.Library()


@register.filter
def which_value(value, what):
    return Preferences.objects.get(value=value, key=what).title
