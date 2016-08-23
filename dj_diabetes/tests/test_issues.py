# coding: utf-8
from datetime import datetime

from dj_diabetes.forms.base import IssuesForm
from dj_diabetes.models.issues import Issues
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
