# coding: utf-8
from datetime import datetime, time
from django.test import TestCase
from django.contrib.auth.models import User

from dj_diabetes.models.appointments import Appointments, AppointmentTypes
from dj_diabetes.forms.base import AppointmentsForm


class AppointmentsTest(TestCase):

    def setUp(self):
        try:
            self.user = User.objects.get(username='john')
        except User.DoesNotExist:
            self.user = User.objects.create_user(
                username='john', email='john@doe.info', password='doe')
            self.appointmentstypes = AppointmentTypes.objects.create(title='checkup')

    def create_appointments(self):
        user = self.user
        appointment_types = self.appointmentstypes
        title = 'A Title'
        body = 'A body'
        date_appointments = datetime.now()
        return Appointments.objects.create(user=user, appointment_types=appointment_types, title=title, body=body,
                                           date_appointments=date_appointments)

    def test_appointments(self):
        s = self.create_appointments()
        self.assertTrue(isinstance(s, Appointments))
        self.assertEqual(s.show(), "%s (date: %s)" % (s.title, s.date_appointments))

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
        data = {'user': ''}
        initial = {'user': self.user}
        form = AppointmentsForm(data=data, initial=initial)
        self.assertFalse(form.is_valid())
