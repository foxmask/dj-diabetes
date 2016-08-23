# coding: utf-8
from datetime import datetime, time

from dj_diabetes.forms.base import ExamsForm
from dj_diabetes.models.exams import Examinations, ExaminationDetails,\
    ExaminationTypes
from dj_diabetes.tests import MainTest


class ExamsTest(MainTest):

    def setUp(self):
        super(ExamsTest, self).setUp()
        self.examtypes = ExaminationTypes.objects.create(title='checkup')

    def create_exams(self):
        return Examinations.objects.create(user=self.user,
                                           examination_types=self.examtypes,
                                           comments='Everything is ok',
                                           date_examinations=datetime.now())

    def create_exams_line(self, examination):
        return ExaminationDetails.objects.create(examination=examination,
                                                 title='Everything is ok',
                                                 value=3.1)

    def test_exams(self):
        s = self.create_exams()
        self.assertTrue(isinstance(s, Examinations))
        self.assertEqual(s.__str__(), "%s (date %s) (comment: %s)" %
                         (s.examination_types, s.date_examinations, s.comments)
                         )

    def test_exams_details(self):
        s = self.create_exams()
        s2 = self.create_exams_line(s)
        self.assertTrue(isinstance(s2, ExaminationDetails))
        self.assertEqual(s2.__str__(), "%s" % s2.title)

    def test_valid_form(self):
        self.create_exams()
        data = {'examination_types': self.examtypes.id,
                'comments': 'everything looks good',
                'date_examinations': datetime.now(),
                'hour_examinations': time()}
        initial = {'user': self.user}
        form = ExamsForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save(self.user))

    def test_invalid_form(self):
        form = ExamsForm()
        self.assertFalse(form.is_valid())
