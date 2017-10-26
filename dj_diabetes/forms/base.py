# coding: utf-8
from dj_diabetes.models import UserProfile, Preferences

from django import forms
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


class UserInstanceMixin(FormMixin):

    def get_form(self, form_class=None):
        form = super(UserInstanceMixin, self).get_form(form_class)
        form.instance.user = self.request.user
        return form
