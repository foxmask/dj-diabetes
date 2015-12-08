# coding: utf-8
from datetime import datetime, time

from django.conf import settings
from dj_diabetes.models import UserProfile, Preferences
from dj_diabetes.models.glucoses import Glucoses

from dj_diabetes.forms.base import GlucosesForm

from dj_diabetes.tests import MainTest


class GlucosesTest(MainTest):

    def setUp(self):
        super(GlucosesTest, self).setUp()
        Preferences.objects.create(key="moment", value="5", title="Midi", created=datetime.now())

    def create_glucoses(self):
        user = self.user
        glucose = 2.5
        comment = 'all is ok'
        date_glucoses = datetime.now()
        hour_glucoses = time()
        return Glucoses.objects.create(user=user,
                                       glucose=glucose,
                                       comment=comment,
                                       date_glucoses=date_glucoses,
                                       hour_glucoses=hour_glucoses)

    def test_glucoses(self):
        s = self.create_glucoses()
        self.assertTrue(isinstance(s, Glucoses))
        self.assertEqual(s.show(), "Glucose: %s Insulin: %s (date: %s)" % (
                                                s.glucose,
                                                s.insulin,
                                                s.date_glucoses))

    def test_valid_form(self):
        u = self.create_glucoses()
        if settings.DJ_DIABETES['insulin'] is True:
            data = {'moment': '5',
                    'comment': 'everything is ok',
                    'glucose': 2,
                    'insulin': 1,
                    'date_glucoses': datetime.now(),
                    'hour_glucoses': time()}
        else:
            data = {'moment': 'midi',
                    'comment': 'everything is ok',
                    'glucose': 2,
                    'date_glucoses': datetime.now(),
                    'hour_glucoses': time()}
        initial = {'user': self.user}
        form = GlucosesForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = GlucosesForm()
        self.assertFalse(form.is_valid())

