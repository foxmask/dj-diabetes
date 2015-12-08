# coding: utf-8
from datetime import datetime, time
from django.test import TestCase

from dj_diabetes.models.foods import Foods

class FoodsTest(TestCase):

    def create_foods(self):
        title = 'Chocolate'
        return Foods.objects.create(title=title)

    def test_foods(self):
        s = self.create_foods()
        self.assertTrue(isinstance(s, Foods))
        self.assertEqual(s.show(), "%s" % s.title)

