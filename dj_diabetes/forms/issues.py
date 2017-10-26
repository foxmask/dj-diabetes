# coding: utf-8
from dj_diabetes.models.issues import Issues

from django import forms


class IssuesForm(forms.ModelForm):
    """
        Issues Form
    """
    question_to = forms.CharField(widget=forms.TextInput(
        {'class': 'form-control'}))
    # to " suit " the HTML textearea
    question = forms.CharField(widget=forms.Textarea(
        {'class': 'form-control', 'rows': '3'}))
    # to " suit " the HTML textearea
    answer = forms.CharField(widget=forms.Textarea(
        {'class': 'form-control', 'rows': '3'}))
    date_answer = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Issues
        fields = ['question', 'question_to', 'answer', 'date_answer']
