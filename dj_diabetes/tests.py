# coding: utf-8
from datetime import datetime, time
from django.test import TestCase
from django.contrib.auth.models import User
from django.conf import settings
from dj_diabetes.models import UserProfile, Preferences
from dj_diabetes.models.appointments import Appointments, AppointmentTypes
from dj_diabetes.models.exams import Examinations, ExaminationDetails, ExaminationTypes
from dj_diabetes.models.foods import Foods
from dj_diabetes.models.glucoses import Glucoses
from dj_diabetes.models.issues import Issues
from dj_diabetes.models.meals import Meals
from dj_diabetes.models.sports import Sports, Exercises
from dj_diabetes.models.weights import Weights

from dj_diabetes.forms.base import UserProfileForm, AppointmentsForm, ExamsForm, GlucosesForm, IssuesForm, MealsForm
from dj_diabetes.forms.base import WeightsForm, ExercisesForm


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


class FoodsTest(TestCase):

    def create_foods(self):
        title = 'Chocolate'
        return Foods.objects.create(title=title)

    def test_foods(self):
        s = self.create_foods()
        self.assertTrue(isinstance(s, Foods))
        self.assertEqual(s.show(), "%s" % s.title)


class GlucosesTest(TestCase):

    def setUp(self):
        try:
            self.user = User.objects.get(username='john')
        except User.DoesNotExist:
            self.user = User.objects.create_user(
                username='john', email='john@doe.info', password='doe')

        Preferences.objects.create(key="moment", value="5", title="Midi", created=datetime.now())

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
        self.assertEqual(s.show(), "Glucose: %s Insulin: %s (date: %s)" % (
                                                s.glucose,
                                                s.insulin,
                                                s.date_glucoses))

    def test_valid_form(self):
        u = self.create_glucoses()
        if settings.DJ_DIABETES['insulin'] is True:
            data = {'moment': '5',
                    'comment': 'everything is ok',
                    'glucose': 2,
                    'insulin': 1,
                    'date_glucoses': datetime.now(),
                    'hour_glucoses': time()}
        else:
            data = {'moment': 'midi',
                    'comment': 'everything is ok',
                    'glucose': 2,
                    'date_glucoses': datetime.now(),
                    'hour_glucoses': time()}
        initial = {'user': self.user}
        form = GlucosesForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'user': ''}
        initial = {'user': self.user}
        form = GlucosesForm(data=data, initial=initial)
        self.assertFalse(form.is_valid())


class IssuesTest(TestCase):

    def setUp(self):
        try:
            self.user = User.objects.get(username='john')
        except User.DoesNotExist:
            self.user = User.objects.create_user(
                username='john', email='john@doe.info', password='doe')

    def create_issues(self):
        user = self.user
        question = 'How does it work ?'
        question_to = 'Dr'
        answer = 'Like a charm'
        return Issues.objects.create(user=user,
                                     question=question,
                                     answer=answer,
                                     question_to=question_to)

    def test_issues(self):
        s = self.create_issues()
        self.assertTrue(isinstance(s, Issues))
        self.assertEqual(s.show(), "%s" % s.question)

    def test_valid_form(self):
        u = self.create_issues()
        data = {'question': 'How ?',
                'question_to': 'Dr',
                'answer': 'Like that',
                'date_answer': datetime.now()}
        initial = {'user': self.user}
        form = IssuesForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'user': ''}
        initial = {'user': self.user}
        form = IssuesForm(data=data, initial=initial)
        self.assertFalse(form.is_valid())


class MealsTest(TestCase):

    def setUp(self):
        try:
            self.user = User.objects.get(username='john')
        except User.DoesNotExist:
            self.user = User.objects.create_user(
                username='john', email='john@doe.info', password='doe')

        Preferences.objects.create(key="meal", value="4", title="Lunch", created=datetime.now())

    def create_meals(self):
        user = self.user
        food = 'Chicken'
        breakfast_lunch_diner = '1'
        return Meals.objects.create(user=user, food=food, breakfast_lunch_diner=breakfast_lunch_diner)

    def test_meals(self):
        s = self.create_meals()
        self.assertTrue(isinstance(s, Meals))
        self.assertEqual(s.show(), "%s (date: %s)" % (s.food, s.date_meals))

    def test_valid_form(self):
        u = self.create_meals()
        data = {'food': 'Chicken', 'breakfast_lunch_diner': '4', 'date_meals': datetime.now(), 'hour_meals': time()}
        initial = {'user': self.user}
        form = MealsForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'user': ''}
        initial = {'user': self.user}
        form = MealsForm(data=data, initial=initial)
        self.assertFalse(form.is_valid())


class SportsTest(TestCase):

    def setUp(self):
        try:
            self.user = User.objects.get(username='john')
        except User.DoesNotExist:
            self.user = User.objects.create_user(
                username='john', email='john@doe.info', password='doe')

    def create_sports(self):
        return Sports.objects.create(title='tennis')

    def create_exercises(self):
        user = self.user
        sports = self.create_sports()
        comment = 'was fun'
        duration = 1
        return Exercises.objects.create(user=user, sports=sports, comment=comment, duration=duration)

    def test_sports(self):
        s = self.create_sports()
        self.assertTrue(isinstance(s, Sports))
        self.assertEqual(s.show(), "%s" % s.title)

    def test_exercises(self):
        s = self.create_exercises()
        self.assertTrue(isinstance(s, Exercises))
        self.assertEqual(s.show(), "%s (duration: %s)" % (s.sports, s.duration))

    def test_valid_form(self):
        u = self.create_exercises()
        data = {'sports': 1, 'comment': 'all is ok', 'duration': 2,
                'date_exercises': datetime.now(), 'hour_exercises': time()}
        initial = {'user': self.user}
        form = ExercisesForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'user': ''}
        initial = {'user': self.user}
        form = ExercisesForm(data=data, initial=initial)
        self.assertFalse(form.is_valid())


class WeightsTest(TestCase):

    def setUp(self):
        try:
            self.user = User.objects.get(username='john')
        except User.DoesNotExist:
            self.user = User.objects.create_user(
                username='john', email='john@doe.info', password='doe')

    def create_weights(self):
        user = self.user
        weight = 80
        date_weights = datetime.now()
        return Weights.objects.create(user=user, weight=weight, date_weights=date_weights)

    def test_weights(self):
        s = self.create_weights()
        self.assertTrue(isinstance(s, Weights))
        self.assertEqual(s.show(), "%s (date: %s)" % (s.weight, s.date_weights))

    def test_valid_form(self):
        u = self.create_weights()
        data = {'weight': 80, 'date_weights': datetime.now()}
        initial = {'user': self.user}
        form = WeightsForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'user': ''}
        initial = {'user': self.user}
        form = WeightsForm(data=data, initial=initial)
        self.assertFalse(form.is_valid())


class UserProfileFormTest(TestCase):

    def setUp(self):
        try:
            self.user = User.objects.get(username='john')
        except User.DoesNotExist:
            self.user = User.objects.create_user(
                username='john', email='john@doe.info', password='doe')

    def create_user(self):
        return UserProfile(user=self.user)

    def test_valid_form(self):
        u = self.create_user()
        data = {'user': u.user,
                'name': 'jane',
                'birth_date': datetime.now(),
                'address': 'place de l etoile',
                'zipcode': '75008',
                'phone': '12',
                'town': 'paris'}
        initial = {'user': self.user}
        form = UserProfileForm(data=data, initial=initial)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'user': '', 'name': ''}
        initial = {'user': self.user}
        form = UserProfileForm(data=data, initial=initial)
        self.assertFalse(form.is_valid())
