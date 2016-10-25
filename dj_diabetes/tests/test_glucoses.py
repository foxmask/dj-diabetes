# coding: utf-8
from datetime import datetime, time

from django.test import RequestFactory

from dj_diabetes.forms.base import GlucosesForm
from dj_diabetes.models import Preferences
from dj_diabetes.models.glucoses import Glucoses
from dj_diabetes.views.glucoses import GlucosesCreateView, GlucosesUpdateView,\
    GlucosesDeleteView
from dj_diabetes.tests import MainTest


class GlucosesTest(MainTest):

    def setUp(self):
        super(GlucosesTest, self).setUp()
        Preferences.objects.create(key="moment",
                                   value="5",
                                   title="Midi",
                                   created=datetime.now())

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
        self.assertEqual(s.__str__(), "Glucose: %s Insulin: %s (date: %s)" % (
                                                s.glucose,
                                                s.insulin,
                                                s.date_glucoses))

    def test_valid_form_insulin(self):
        self.create_glucoses()
        data = {'moment': '5',
                'comment': 'everything is ok',
                'glucose': 2,
                'insulin': 1,
                'date_glucoses': datetime.now(),
                'hour_glucoses': time()}
        initial = {'user': self.user}
        form = GlucosesForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = GlucosesForm()
        self.assertFalse(form.is_valid())


class GlucosesCreateViewTestCase(GlucosesTest):

    def test_get(self):
        template = "dj_diabetes/glucoses_form.html"
        # Setup request and view.
        request = RequestFactory().get('glucoses/')
        request.user = self.user
        view = GlucosesCreateView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         "dj_diabetes/glucoses_form.html")


class GlucosesUpdateViewTestCase(GlucosesTest):

    def test_get(self):
        app = self.create_glucoses()
        template = "dj_diabetes/glucoses_form.html"
        # Setup request and view.
        request = RequestFactory().get('glucoses/edit/{}'.format(app.id))
        request.user = self.user
        view = GlucosesUpdateView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user, pk=app.id)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         "dj_diabetes/glucoses_form.html")


class GlucosesDeleteViewTestCase(GlucosesTest):

    def test_get(self):
        app = self.create_glucoses()
        template = 'dj_diabetes/confirm_delete.html'
        # Setup request and view.
        request = RequestFactory().get('glucoses/delete/{}'.format(app.id))
        request.user = self.user
        view = GlucosesDeleteView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user, pk=app.id)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         'dj_diabetes/confirm_delete.html')
