# coding: utf-8
from dj_diabetes.forms.base import pref_filter
from dj_diabetes.models.meals import Meals

from django import forms


class MealsForm(forms.ModelForm):
    """
        Meals Form
    """
    # get the list of pref to get the value in the dropdown
    breakfast_lunch_diner = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}))
    food = forms.CharField(widget=forms.Textarea(
        {'class': 'form-control', 'rows': '3'}))
    date_meals = forms.DateField(widget=forms.TextInput(
        {'class': 'form-control'}))
    hour_meals = forms.TimeField(widget=forms.TextInput(
        {'class': 'form-control'}))

    class Meta:
        model = Meals
        fields = ['food', 'breakfast_lunch_diner', 'date_meals', 'hour_meals']

    def __init__(self, *args, **kwargs):
        super(MealsForm, self).__init__(*args, **kwargs)
        self.fields['breakfast_lunch_diner'].choices = pref_filter("meal")
