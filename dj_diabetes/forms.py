# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.forms.models import inlineformset_factory
#from django.forms.formsets import inlineformset_factory

from dj_diabetes.models import Glucoses, Appointments, Sports, Foods, Meals
from dj_diabetes.models import ExaminationTypes, AppointmentTypes, Issues
from dj_diabetes.models import Weights, Exercises, Preferences
from dj_diabetes.models import Examinations, ExaminationDetails

# Function


def pref_filter(filter):
    """
        get the value we have in the Preferences model for a given key
    """
    choices = Preferences.objects.filter(key=filter)
    data = ()
    all_data = ()
    for choice in choices:
        data = (int(choice.value), choice.title)
        all_data = (data,) + all_data
    return all_data


# Non-ADMIN FORMS Part


class GlucosesForm(forms.ModelForm):
    """
        glucoses Form
    """
    # get the list of pref to get the value in the dropdow
    moment = forms.ChoiceField(pref_filter("moment"))
    # to " suit " the HTML textearea
    comment = forms.CharField(widget=forms.Textarea(
        {'class': 'form-control', 'rows': '3'}))

    class Meta:
        model = Glucoses
        # Do the user uses insulin ?
        if settings.DJ_DIABETES['insulin'] is True:
            fields = ['moment', 'comment', 'glucose', 'insulin',
                      'date_glucose', 'hour_glucose']
        else:
            fields = ['moment', 'comment', 'glucose',
                      'date_glucose', 'hour_glucose']


class AppointmentsForm(forms.ModelForm):
    """
        Appointments Form
    """
    # to " suit " the HTML textearea
    body = forms.CharField(widget=forms.Textarea(
        {'class': 'form-control', 'rows': '3'}))

    class Meta:
        model = Appointments
        fields = ['appointment_types', 'title', 'body',
                  'date_appointment', 'hour_appointment',
                  'recall_one_duration', 'recall_two_duration',
                  'recall_one_unit', 'recall_two_unit']


class IssuesForm(forms.ModelForm):
    """
        Issues Form
    """
    # to " suit " the HTML textearea
    question = forms.CharField(widget=forms.Textarea(
        {'class': 'form-control', 'rows': '3'}))
    # to " suit " the HTML textearea
    answer = forms.CharField(widget=forms.Textarea(
        {'class': 'form-control', 'rows': '3'}))

    class Meta:
        model = Issues
        fields = ['question', 'question_to', 'answer', 'date_answer']


class WeightsForm(forms.ModelForm):
    """
        Weights Form
    """
    class Meta:
        model = Weights
        fields = ['weight', 'date_weight']


class MealsForm(forms.ModelForm):
    """
        Meals Form
    """
    # get the list of pref to get the value in the dropdow
    breakfast_lunch_diner = forms.ChoiceField(pref_filter("meal"))
    food = forms.CharField(widget=forms.Textarea(
        {'class': 'form-control', 'rows': '3'}))

    class Meta:
        model = Meals
        fields = ['food', 'breakfast_lunch_diner', 'date_meal', 'hour_meal']


class ExercisesForm(forms.ModelForm):
    """
        Exercises Form
    """
    comment = forms.CharField(widget=forms.Textarea(
        {'class': 'form-control', 'rows': '3'}))

    class Meta:
        model = Exercises
        fields = ['sports', 'comment', 'duration',
                  'date_exercise', 'hour_exercise']


class ExamsForm(forms.ModelForm):
    """
        Exams Form
    """
    # to " suit " the HTML textearea
    comments = forms.CharField(widget=forms.Textarea(
        {'class': 'form-control', 'rows': '3'}))

    class Meta:
        model = Examinations
        fields = ['examination_types', 'comments',
                  'date_examination', 'hour_examination']


class ExamDetailsForm(forms.ModelForm):
    """
        Details of Exams Form
    """
    class Meta:
        model = ExaminationDetails
        fields = ['title', 'value']

# a formeset based on the model of the Mother and Child + 2 new empty lines
ExamDetailsFormSet = inlineformset_factory(Examinations, ExaminationDetails, extra=2)


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
