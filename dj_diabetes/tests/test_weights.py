# coding: utf-8
from datetime import datetime

from django.test import RequestFactory

from dj_diabetes.forms.base import WeightsForm
from dj_diabetes.models.weights import Weights
from dj_diabetes.views.weights import WeightsCreateView, WeightsUpdateView, \
    WeightsDeleteView
from dj_diabetes.tests import MainTest


class WeightsTest(MainTest):

    def setUp(self):
        super(WeightsTest, self).setUp()

        user = self.user
        weight = 80
        date_weights = datetime.now()
        self.weights = Weights.objects.create(user=user,
                                              weight=weight,
                                              date_weights=date_weights)

    def test_weights(self):
        self.assertTrue(isinstance(self.weights, Weights))
        self.assertEqual(self.weights .__str__(), "%s (date: %s)" %
                         (self.weights .weight, self.weights .date_weights))

    def test_valid_form(self):
        data = {'weight': 80, 'date_weights': datetime.now()}
        initial = {'user': self.user}
        form = WeightsForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = WeightsForm()
        self.assertFalse(form.is_valid())


class WeightsCreateViewTestCase(WeightsTest):

    def test_get(self):
        template = "dj_diabetes/weights_form.html"
        # Setup request and view.
        request = RequestFactory().get('weights/')
        request.user = self.user
        view = WeightsCreateView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         "dj_diabetes/weights_form.html")


class WeightsUpdateViewTestCase(WeightsTest):

    def test_get(self):
        template = "dj_diabetes/weights_form.html"
        # Setup request and view.
        request = RequestFactory().get('weights/edit/{}'.format(
            self.weights.id))
        request.user = self.user
        view = WeightsUpdateView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user, pk=self.weights.id)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         "dj_diabetes/weights_form.html")


class WeightsDeleteViewTestCase(WeightsTest):

    def test_get(self):
        template = 'dj_diabetes/confirm_delete.html'
        # Setup request and view.
        request = RequestFactory().get('weights/delete/{}'.format(
            self.weights.id))
        request.user = self.user
        view = WeightsDeleteView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user, pk=self.weights.id)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         'dj_diabetes/confirm_delete.html')
