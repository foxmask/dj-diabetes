# coding: utf-8
from datetime import datetime

from dj_diabetes.forms.base import WeightsForm
from dj_diabetes.models.weights import Weights
from dj_diabetes.tests import MainTest


class WeightsTest(MainTest):

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
        form = WeightsForm( )
        self.assertFalse(form.is_valid())
