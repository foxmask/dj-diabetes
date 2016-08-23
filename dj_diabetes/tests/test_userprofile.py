# coding: utf-8
from datetime import datetime

from dj_diabetes.forms.base import UserProfileForm
from dj_diabetes.models import UserProfile, Preferences
from dj_diabetes.tests import MainTest


class UserProfileTest(MainTest):

    def setUp(self):
        super(UserProfileTest, self).setUp()
        self.userprofile = UserProfile(user=self.user)

    def test_display_user(self):
        self.assertEqual(self.userprofile.__str__(), self.user.__str__())

    def test_valid_form(self):
        data = {'user': self.userprofile,
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
        form = UserProfileForm()
        self.assertFalse(form.is_valid())


class PreferenceTest(MainTest):

    def setUp(self):
        super(PreferenceTest, self).setUp()
        self.preference = Preferences.objects.create(title="foobar",
                                                     key="foo",
                                                     value="bar")

    def test_display_pref(self):
        self.assertEqual(self.preference.__str__(), "%s %s %s" % (
            self.preference.key, self.preference.title, self.preference.value))
