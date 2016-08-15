# coding: utf-8
from dj_diabetes.models import Preferences
from dj_diabetes.models.appointments import AppointmentTypes
from dj_diabetes.models.exams import ExaminationTypes
from dj_diabetes.models.foods import Foods
from dj_diabetes.models.sports import Sports

from django import forms


# ADMIN FORMS Part
class ExaminationTypesAdminForm(forms.ModelForm):
    """
        Manage the examination types
    """
    class Meta:
        model = ExaminationTypes
        fields = ['title']


class AppointmentTypesAdminForm(forms.ModelForm):

    """
        Manage the appointment types
    """
    class Meta:
        model = AppointmentTypes
        fields = ['title']


class FoodsAdminForm(forms.ModelForm):

    """
        Manage the Foods
    """
    class Meta:
        model = Foods
        fields = ['title']


class SportsAdminForm(forms.ModelForm):

    """
        Manage the sports
    """
    class Meta:
        model = Sports
        fields = ['title']


class PrefAdminForm(forms.ModelForm):

    """
        Manage the preferences
    """
    class Meta:
        model = Preferences
        fields = ['key', 'title', 'value']
