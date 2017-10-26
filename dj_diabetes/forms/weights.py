# coding: utf-8
from dj_diabetes.models.weights import Weights

from django import forms


class WeightsForm(forms.ModelForm):
    """
        Weights Form
    """
    weight = forms.IntegerField(widget=forms.TextInput(
        {'class': 'form-control', 'type': 'number'}))
    date_weights = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Weights
        fields = ['weight', 'date_weights']
