# coding: utf-8
from datetime import datetime, time

from django.test import RequestFactory

from dj_diabetes.forms.base import AppointmentsForm
from dj_diabetes.models.appointments import Appointments, AppointmentTypes
from dj_diabetes.views.appointments import AppointmentsCreateView,\
    AppointmentsUpdateView, AppointmentsDeleteView
from dj_diabetes.tests import MainTest


class AppointmentsTest(MainTest):

    def setUp(self):
        super(AppointmentsTest, self).setUp()
        self.appointmentstypes = AppointmentTypes.objects.create(
            title='checkup')

    def create_appointments(self):
        user = self.user
        appointment_types = self.appointmentstypes
        title = 'A Title'
        body = 'A body'
        date_appointments = datetime.now()
        return Appointments.objects.create(user=user,
                                           appointment_types=appointment_types,
                                           title=title,
                                           body=body,
                                           date_appointments=date_appointments)

    def test_appointments(self):
        s = self.create_appointments()
        self.assertTrue(isinstance(s, Appointments))
        self.assertEqual(s.__str__(), "%s (date: %s)" % (s.title,
                                                         s.date_appointments))

    def test_valid_form(self):
        u = self.create_appointments()
        data = {'appointment_types': 1,
                'user': u.user,
                'title': 'complet checkup',
                'body': 'everything is ok',
                'recall_one_duration': 1,
                'recall_two_duration': 2,
                'recall_one_unit': 1,
                'recall_two_unit': 2,
                'date_appointments': datetime.now(),
                'hour_appointments': time()}
        initial = {'user': self.user}
        form = AppointmentsForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = AppointmentsForm()
        self.assertFalse(form.is_valid())


class AppointmentsCreateViewTestCase(AppointmentsTest):

    def test_get(self):
        template = "dj_diabetes/appointments_form.html"
        # Setup request and view.
        request = RequestFactory().get('appoints/')
        request.user = self.user
        view = AppointmentsCreateView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         "dj_diabetes/appointments_form.html")


class AppointmentsUpdateViewTestCase(AppointmentsTest):

    def test_get(self):
        app = self.create_appointments()
        template = "dj_diabetes/appointments_form.html"
        # Setup request and view.
        request = RequestFactory().get('appoints/edit/{}'.format(app.id))
        request.user = self.user
        view = AppointmentsUpdateView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user, pk=app.id)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         "dj_diabetes/appointments_form.html")


class AppointmentsDeleteViewTestCase(AppointmentsTest):

    def test_get(self):
        app = self.create_appointments()
        template = 'dj_diabetes/confirm_delete.html'
        # Setup request and view.
        request = RequestFactory().get('appoints/delete/{}'.format(app.id))
        request.user = self.user
        view = AppointmentsDeleteView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user, pk=app.id)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         'dj_diabetes/confirm_delete.html')
