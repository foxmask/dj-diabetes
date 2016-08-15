# coding: utf-8
from datetime import datetime, time

from dj_diabetes.forms.base import MealsForm
from dj_diabetes.models import Preferences
from dj_diabetes.models.meals import Meals
from dj_diabetes.tests import MainTest


class MealsTest(MainTest):

    def setUp(self):
        super(MealsTest, self).setUp()
        Preferences.objects.create(key="meal", value="4", title="Lunch", created=datetime.now())

    def create_meals(self):
        user = self.user
        food = 'Chicken'
        breakfast_lunch_diner = '1'
        return Meals.objects.create(user=user, food=food, breakfast_lunch_diner=breakfast_lunch_diner)

    def test_meals(self):
        s = self.create_meals()
        self.assertTrue(isinstance(s, Meals))
        self.assertEqual(s.show(), "%s (date: %s)" % (s.food, s.date_meals))

    def test_valid_form(self):
        u = self.create_meals()
        data = {'food': 'Chicken', 'breakfast_lunch_diner': '4', 'date_meals': datetime.now(), 'hour_meals': time()}
        initial = {'user': self.user}
        form = MealsForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = MealsForm()
        self.assertFalse(form.is_valid())


