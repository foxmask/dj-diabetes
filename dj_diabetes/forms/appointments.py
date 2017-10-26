# coding: utf-8
from dj_diabetes.models.appointments import Appointments

from django import forms


class AppointmentsForm(forms.ModelForm):
    """
        Appointments Form
    """
    # to " suit " the HTML textearea
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '3'}))
    recall_one_duration = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'number'}))
    recall_two_duration = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'number'}))
    recall_one_unit = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'number'}))
    recall_two_unit = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'number'}))
    date_appointments = forms.DateField(widget=forms.TextInput(
        {'class': 'form-control'}))
    hour_appointments = forms.TimeField(widget=forms.TextInput(
        {'class': 'form-control'}))

    class Meta:
        model = Appointments
        fields = ['appointment_types', 'title', 'body',
                  'date_appointments', 'hour_appointments',
                  'recall_one_duration', 'recall_two_duration',
                  'recall_one_unit', 'recall_two_unit']

    def __init__(self, *args, **kwargs):
        super(AppointmentsForm, self).__init__(*args, **kwargs)
        self.fields['appointment_types'].widget.attrs['class'] = 'form-control'
