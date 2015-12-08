# coding: utf-8
from datetime import datetime, time
from django.test import TestCase
from django.contrib.auth.models import User

from dj_diabetes.models.weights import Weights
from dj_diabetes.forms.base import WeightsForm


class WeightsTest(TestCase):

    def setUp(self):
        try:
            self.user = User.objects.get(username='john')
        except User.DoesNotExist:
            self.user = User.objects.create_user(
                username='john', email='john@doe.info', password='doe')

    def create_weights(self):
        user = self.user
        weight = 80
        date_weights = datetime.now()
        return Weights.objects.create(user=user, weight=weight, date_weights=date_weights)

    def test_weights(self):
        s = self.create_weights()
        self.assertTrue(isinstance(s, Weights))
        self.assertEqual(s.show(), "%s (date: %s)" % (s.weight, s.date_weights))

    def test_valid_form(self):
        u = self.create_weights()
        data = {'weight': 80, 'date_weights': datetime.now()}
        initial = {'user': self.user}
        form = WeightsForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'user': ''}
        initial = {'user': self.user}
        form = WeightsForm(data=data, initial=initial)
        self.assertFalse(form.is_valid())
