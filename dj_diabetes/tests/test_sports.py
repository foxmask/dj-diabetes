# coding: utf-8
from datetime import datetime, time

from django.test import RequestFactory

from dj_diabetes.forms.base import ExercisesForm
from dj_diabetes.models.sports import Sports, Exercises
from dj_diabetes.tests import MainTest
from dj_diabetes.views.exercises import ExercisesCreateView,\
    ExercisesUpdateView, ExercisesDeleteView


class SportsTest(MainTest):

    def setUp(self):
        super(SportsTest, self).setUp()
        self.sport = Sports.objects.create(title='tennis')

    def create_exercises(self):
        user = self.user
        comment = 'was fun'
        duration = 1
        return Exercises.objects.create(user=user,
                                        sports=self.sport,
                                        comment=comment,
                                        duration=duration)

    def test_sports(self):
        self.assertTrue(isinstance(self.sport, Sports))
        self.assertEqual(self.sport.__str__(), "%s" % self.sport.title)

    def test_exercises(self):
        s = self.create_exercises()
        self.assertTrue(isinstance(s, Exercises))
        self.assertEqual(s.__str__(), "%s (duration: %s)" %
                         (s.sports, s.duration))

    def test_valid_form(self):
        self.create_exercises()
        data = {'sports': 1, 'comment': 'all is ok', 'duration': 2,
                'date_exercises': datetime.now(), 'hour_exercises': time()}
        initial = {'user': self.user}
        form = ExercisesForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = ExercisesForm()
        self.assertFalse(form.is_valid())


class ExercisesCreateViewTestCase(SportsTest):

    def test_get(self):
        template = "dj_diabetes/exercises_form.html"
        # Setup request and view.
        request = RequestFactory().get('exercises/')
        request.user = self.user
        view = ExercisesCreateView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         "dj_diabetes/exercises_form.html")


class ExercisesUpdateViewTestCase(SportsTest):

    def test_get(self):
        app = self.create_exercises()
        template = "dj_diabetes/exercises_form.html"
        # Setup request and view.
        request = RequestFactory().get('exercises/edit/{}'.format(app.id))
        request.user = self.user
        view = ExercisesUpdateView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user, pk=app.id)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         "dj_diabetes/exercises_form.html")


class ExercisesDeleteViewTestCase(SportsTest):

    def test_get(self):
        app = self.create_exercises()
        template = 'dj_diabetes/confirm_delete.html'
        # Setup request and view.
        request = RequestFactory().get('exercises/delete/{}'.format(app.id))
        request.user = self.user
        view = ExercisesDeleteView.as_view(template_name=template)
        # Run.
        response = view(request, user=request.user, pk=app.id)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0],
                         'dj_diabetes/confirm_delete.html')
