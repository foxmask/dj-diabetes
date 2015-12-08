# coding: utf-8
from datetime import datetime, time
from django.test import TestCase
from django.contrib.auth.models import User

from dj_diabetes.models.exams import Examinations, ExaminationDetails, ExaminationTypes
from dj_diabetes.forms.base import ExamsForm


class ExamsTest(TestCase):
    def setUp(self):
        try:
            self.user = User.objects.get(username='john')
        except User.DoesNotExist:
            self.user = User.objects.create_user(
                username='john', email='john@doe.info', password='doe')
            self.examtypes = ExaminationTypes.objects.create(title='checkup')

    def create_exams(self):
        return Examinations.objects.create(user=self.user, examination_types=self.examtypes, comments='Everything is ok',
                                           date_examinations=datetime.now())

    def create_exams_line(self, examination):
        return ExaminationDetails.objects.create(examination=examination,
                                                 title='Everything is ok',
                                                 value=3.1)

    def test_exams(self):
        s = self.create_exams()
        self.assertTrue(isinstance(s, Examinations))
        self.assertEqual(s.show(), "%s (date %s) (comment: %s)" % (s.examination_types, s.date_examinations, s.comments))

    def test_exams_details(self):
        s = self.create_exams()
        s2 = self.create_exams_line(s)
        self.assertTrue(isinstance(s2, ExaminationDetails))
        self.assertEqual(s2.show(), "%s" % s2.title)

    def test_valid_form(self):
        u = self.create_exams()
        data = {'examination_types': self.examtypes.id,
                'comments': 'everything looks good',
                'date_examinations': datetime.now(),
                'hour_examinations': time()}
        initial = {'user': self.user}
        form = ExamsForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'user': ''}
        initial = {'user': self.user}
        form = ExamsForm(data=data, initial=initial)
        self.assertFalse(form.is_valid())
