# coding: utf-8
from dj_diabetes.models.sports import Exercises

from django import forms


class ExercisesForm(forms.ModelForm):
    """
        Exercises Form
    """
    comment = forms.CharField(widget=forms.Textarea(
        {'class': 'form-control', 'rows': '3'}))
    duration = forms.IntegerField(widget=forms.TextInput(
        {'class': 'form-control', 'type': 'number'}))
    date_exercises = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    hour_exercises = forms.TimeField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Exercises
        fields = ['sports', 'comment', 'duration',
                  'date_exercises', 'hour_exercises']

    def __init__(self, *args, **kwargs):
        super(ExercisesForm, self).__init__(*args, **kwargs)
        self.fields['sports'].widget.attrs['class'] = 'form-control'
