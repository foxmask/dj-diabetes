# coding: utf-8
from datetime import datetime, time

from django.test import RequestFactory

from dj_diabetes.forms.base import MealsForm
from dj_diabetes.models import Preferences
from dj_diabetes.models.meals import Meals
from dj_diabetes.views.meals import MealsCreateView, MealsUpdateView, \
    MealsDeleteView
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


class MealsCreateViewTestCase(MealsTest):

    def test_get(self):
        template = "dj_diabetes/meals_form.html"
        # Setup request and view.
        request = RequestFactory().get('meals/')
        request.user = self.user
        view = MealsCreateView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         "dj_diabetes/meals_form.html")


class MealsUpdateViewTestCase(MealsTest):

    def test_get(self):
        template = "dj_diabetes/meals_form.html"
        # Setup request and view.
        request = RequestFactory().get('meals/edit/{}'.format(
            self.meals.id))
        request.user = self.user
        view = MealsUpdateView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user, pk=self.meals.id)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         "dj_diabetes/meals_form.html")


class MealsDeleteViewTestCase(MealsTest):

    def test_get(self):
        template = 'dj_diabetes/confirm_delete.html'
        # Setup request and view.
        request = RequestFactory().get('meals/delete/{}'.format(
            self.meals.id))
        request.user = self.user
        view = MealsDeleteView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user, pk=self.meals.id)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         'dj_diabetes/confirm_delete.html')
