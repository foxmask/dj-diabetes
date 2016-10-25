# coding: utf-8
from datetime import datetime

from django.test import RequestFactory

from dj_diabetes.forms.base import IssuesForm
from dj_diabetes.models.issues import Issues
from dj_diabetes.views.issues import IssuesCreateView, IssuesUpdateView,\
    IssuesDeleteView
from dj_diabetes.tests import MainTest


class IssuesTest(MainTest):

    def setUp(self):
        super(IssuesTest, self).setUp()
        user = self.user
        question = 'How does it work ?'
        question_to = 'Dr'
        answer = 'Like a charm'
        self.issues = Issues.objects.create(user=user,
                                            question=question,
                                            answer=answer,
                                            question_to=question_to)

    def test_issues(self):
        self.assertTrue(isinstance(self.issues, Issues))
        self.assertEqual(self.issues.__str__(), "%s" % self.issues.question)

    def test_valid_form(self):
        data = {'question': 'How ?',
                'question_to': 'Dr',
                'answer': 'Like that',
                'date_answer': datetime.now()}
        initial = {'user': self.user}
        form = IssuesForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = IssuesForm()
        self.assertFalse(form.is_valid())


class IssuesCreateViewTestCase(IssuesTest):

    def test_get(self):
        template = "dj_diabetes/issues_form.html"
        # Setup request and view.
        request = RequestFactory().get('issues/')
        request.user = self.user
        view = IssuesCreateView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         "dj_diabetes/issues_form.html")


class IssuesUpdateViewTestCase(IssuesTest):

    def test_get(self):
        template = "dj_diabetes/issues_form.html"
        # Setup request and view.
        request = RequestFactory().get('issues/edit/{}'.format(self.issues.id))
        request.user = self.user
        view = IssuesUpdateView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user, pk=self.issues.id)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         "dj_diabetes/issues_form.html")


class IssuesDeleteViewTestCase(IssuesTest):

    def test_get(self):
        template = 'dj_diabetes/confirm_delete.html'
        # Setup request and view.
        request = RequestFactory().get('issues/delete/{}'.format(
            self.issues.id))
        request.user = self.user
        view = IssuesDeleteView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user, pk=self.issues.id)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         'dj_diabetes/confirm_delete.html')
