# coding: utf-8
from datetime import datetime, time

from django.test import RequestFactory

from dj_diabetes.forms.base import ExamsForm
from dj_diabetes.models.exams import Examinations, ExaminationDetails,\
    ExaminationTypes
from dj_diabetes.views.exams import ExamsCreateView, ExamsUpdateView, \
    ExamsDeleteView
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


class ExamsCreateViewTestCase(ExamsTest):

    def test_get(self):
        template = "dj_diabetes/exams_form.html"
        # Setup request and view.
        request = RequestFactory().get('exams/')
        request.user = self.user
        view = ExamsCreateView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         "dj_diabetes/exams_form.html")


class ExamsUpdateViewTestCase(ExamsTest):

    def test_get(self):
        app = self.create_exams()
        template = "dj_diabetes/exams_form.html"
        # Setup request and view.
        request = RequestFactory().get('exams/edit/{}'.format(app.id))
        request.user = self.user
        view = ExamsUpdateView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user, pk=app.id)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         "dj_diabetes/exams_form.html")


class ExamsDeleteViewTestCase(ExamsTest):

    def test_get(self):
        app = self.create_exams()
        template = 'dj_diabetes/confirm_delete.html'
        # Setup request and view.
        request = RequestFactory().get('exams/delete/{}'.format(app.id))
        request.user = self.user
        view = ExamsDeleteView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user, pk=app.id)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         'dj_diabetes/confirm_delete.html')
