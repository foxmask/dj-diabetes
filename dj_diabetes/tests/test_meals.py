# coding: utf-8
from datetime import datetime, time

from dj_diabetes.forms.base import MealsForm
from dj_diabetes.models import Preferences
from dj_diabetes.models.meals import Meals
from dj_diabetes.tests import MainTest


class MealsTest(MainTest):

    def setUp(self):
        super(MealsTest, self).setUp()
        Preferences.objects.create(key="meal",
                                   value="4",
                                   title="Lunch",
                                   created=datetime.now())
        user = self.user
        food = 'Chicken'
        self.meals = Meals.objects.create(user=user, food=food,
                                          breakfast_lunch_diner=1)

    def test_meals(self):
        self.assertTrue(isinstance(self.meals, Meals))
        self.assertEqual(self.meals.__str__(), "%s (date: %s)" %
                         (self.meals.food, self.meals.date_meals))

    def test_valid_form(self):
        data = {'food': 'Chicken', 'breakfast_lunch_diner': '4',
                'date_meals': datetime.now(), 'hour_meals': time()}
        initial = {'user': self.user}
        form = MealsForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = MealsForm()
        self.assertFalse(form.is_valid())
