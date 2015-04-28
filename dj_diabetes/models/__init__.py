# coding: utf-8
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

from appointments import AppointmentTypes, Appointments
from exams import Examinations, ExaminationTypes, ExaminationDetails
from foods import Foods
from glucoses import Glucoses
from issues import Issues
from meals import Meals
from sports import Sports, Exercises
from weights import Weights



@python_2_unicode_compatible
class UserProfile(models.Model):

    """
        Related user to handle his profile
    """
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(null=True, blank=True)
    zipcode = models.CharField(max_length=50, blank=True)
    town = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # active = models.BooleanField()

    def show(self):
        return "User profile %s" % (self.user_id)

    def __str__(self):
        return "%s" % (self.user)


class Preferences(models.Model):

    """
        Preferences
    """
    key = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    value = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Preference'
        verbose_name_plural = 'Preferences'

    def show(self):
        return "Preferences %s %s %s %s %s" % (self.key, self.title,
                                               self.value,
                                               self.created, self.modified)

    def __str__(self):
        return "%s %s %s" % (self.key, self.title, self.value)


def create_user_profile(sender, instance, created, **kwargs):
    """
        function to create the record in the UserProfile model
    """
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

