# coding: utf-8
from datetime import datetime, time
from django.test import TestCase
from django.contrib.auth.models import User

from dj_diabetes.models.sports import Sports, Exercises
from dj_diabetes.forms.base import ExercisesForm


class SportsTest(TestCase):

    def setUp(self):
        try:
            self.user = User.objects.get(username='john')
        except User.DoesNotExist:
            self.user = User.objects.create_user(
                username='john', email='john@doe.info', password='doe')

    def create_sports(self):
        return Sports.objects.create(title='tennis')

    def create_exercises(self):
        user = self.user
        sports = self.create_sports()
        comment = 'was fun'
        duration = 1
        return Exercises.objects.create(user=user, sports=sports, comment=comment, duration=duration)

    def test_sports(self):
        s = self.create_sports()
        self.assertTrue(isinstance(s, Sports))
        self.assertEqual(s.show(), "%s" % s.title)

    def test_exercises(self):
        s = self.create_exercises()
        self.assertTrue(isinstance(s, Exercises))
        self.assertEqual(s.show(), "%s (duration: %s)" % (s.sports, s.duration))

    def test_valid_form(self):
        u = self.create_exercises()
        data = {'sports': 1, 'comment': 'all is ok', 'duration': 2,
                'date_exercises': datetime.now(), 'hour_exercises': time()}
        initial = {'user': self.user}
        form = ExercisesForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'user': ''}
        initial = {'user': self.user}
        form = ExercisesForm(data=data, initial=initial)
        self.assertFalse(form.is_valid())

