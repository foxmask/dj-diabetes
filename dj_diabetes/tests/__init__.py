# coding: utf-8
from datetime import datetime

from dj_diabetes.forms.base import UserProfileForm
from dj_diabetes.models import UserProfile

from django.contrib.auth.models import User
from django.test import TestCase


class MainTest(TestCase):

    def setUp(self):
        try:
            self.user = User.objects.get(username='john')
        except User.DoesNotExist:
            self.user = User.objects.create_user(
                username='john', email='john@doe.info', password='doe')


class UserProfileFormTest(MainTest):

    def create_user(self):
        return UserProfile(user=self.user)

    def test_valid_form(self):
        u = self.create_user()
        data = {'user': u.user,
                'name': 'jane',
                'birth_date': datetime.now(),
                'address': 'place de l etoile',
                'zipcode': '75008',
                'phone': '12',
                'town': 'paris'}
        initial = {'user': self.user}
        form = UserProfileForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = UserProfileForm()
        self.assertFalse(form.is_valid())
