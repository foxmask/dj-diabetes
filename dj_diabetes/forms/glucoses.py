# coding: utf-8
from dj_diabetes.forms.base import pref_filter
from dj_diabetes.models.glucoses import Glucoses


from django import forms
from django.conf import settings


class GlucosesForm(forms.ModelForm):
    """
        glucoses Form
    """
    glucose = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'number'}))
    # get the list of pref to get the value in the dropdown
    insulin = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'number'}))
    moment = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}))
    # to " suit " the HTML textearea
    comment = forms.CharField(widget=forms.Textarea(
        {'class': 'form-control', 'rows': '3'}))
    date_glucoses = forms.DateField(widget=forms.TextInput(
        {'class': 'form-control'}))
    hour_glucoses = forms.TimeField(widget=forms.TextInput(
        {'class': 'form-control'}))

    class Meta:
        model = Glucoses
        # Do the user uses insulin ?
        if settings.DJ_DIABETES['insulin'] is True:
            fields = ['moment', 'comment', 'glucose', 'insulin',
                      'date_glucoses', 'hour_glucoses']
        else:
            fields = ['moment', 'comment', 'glucose',
                      'date_glucoses', 'hour_glucoses']

    def __init__(self, *args, **kwargs):
        super(GlucosesForm, self).__init__(*args, **kwargs)
        self.fields['moment'].choices = pref_filter("moment")
