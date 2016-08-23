# coding: utf-8
from dj_diabetes.models import UserProfile, Preferences
from dj_diabetes.models.appointments import Appointments
from dj_diabetes.models.exams import Examinations, ExaminationDetails
from dj_diabetes.models.glucoses import Glucoses
from dj_diabetes.models.issues import Issues
from dj_diabetes.models.meals import Meals
from dj_diabetes.models.sports import Exercises
from dj_diabetes.models.weights import Weights

from django import forms
from django.conf import settings
from django.forms.models import inlineformset_factory
from django.views.generic.edit import FormMixin


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


class UserProfileForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        {'class': 'form-control'}))
    birth_date = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(
        {'type': 'tel', 'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(
        {'class': 'form-control', 'rows': '3'}))
    zipcode = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    town = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ['name', 'birth_date', 'phone',
                  'address', 'zipcode', 'town']


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


class UserInstanceMixin(FormMixin):

    def get_form(self, form_class=None):
        form = super(UserInstanceMixin, self).get_form(form_class)
        form.instance.user = self.request.user
        return form
