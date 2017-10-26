# coding: utf-8
from dj_diabetes.models.exams import Examinations, ExaminationDetails

from django import forms
from django.forms.models import inlineformset_factory


class ExamsForm(forms.ModelForm):
    """
        Exams Form
    """
    # to " suit " the HTML textearea
    comments = forms.CharField(widget=forms.Textarea(
        {'class': 'form-control', 'rows': '3'}))
    date_examinations = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    hour_examinations = forms.TimeField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    def save(self, user=None):
        self.myobject = super(ExamsForm, self).save(commit=False)
        self.myobject.user = user
        self.myobject.save()
        return self.myobject

    class Meta:
        model = Examinations
        fields = ['examination_types', 'comments',
                  'date_examinations', 'hour_examinations']
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(ExamsForm, self).__init__(*args, **kwargs)
        self.fields['examination_types'].widget.attrs['class'] = 'form-control'


class ExamDetailsForm(forms.ModelForm):
    """
        Details of Exams Form
    """
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    value = forms.DecimalField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'number'}))

    class Meta:
        model = ExaminationDetails
        fields = ['title', 'value']


# a formset based on the model of the Mother and Child + 2 new empty lines
my_fields = ('examination', 'title', 'value')
ExamDetailsFormSet = inlineformset_factory(Examinations,
                                           ExaminationDetails,
                                           fields=my_fields, extra=2)
