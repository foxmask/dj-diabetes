# coding: utf-8
from django.contrib.auth.models import User

from dj_diabetes.views import round_value
from django.test import TestCase


class MainTest(TestCase):

    def setUp(self):
        try:
            self.user = User.objects.get(username='john')
        except User.DoesNotExist:
            self.user = User.objects.create_user(
                username='john', email='john@doe.info', password='doe')


class ViewsTest(TestCase):

    def test_round_value(self):
        self.assertEqual(round_value(7.46), 7.5)
        self.assertEqual(round_value(7.16), 7.2)
        self.assertEqual(round_value(7.11), 7.1)
