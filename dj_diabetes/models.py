# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):

    """
        Related user to handle his profile
    """
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    zipcode = models.CharField(max_length=50)
    town = models.CharField(max_length=255)
    role = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # active = models.BooleanField()

    def show(self):
        return "User profile %s" % (self.user_id)

    def __unicode__(self):
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

    def __unicode__(self):
        return "%s %s %s" % (self.key, self.title, self.value)


class Issues(models.Model):

    """
        Issues asked from the user
    """
    user = models.ForeignKey(User)
    question = models.TextField()
    question_to = models.CharField(max_length=255)
    answer = models.TextField(null=True, blank=True)
    date_answer = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Issues'
        verbose_name_plural = 'Issues'

    def show(self):
        return "Issues %s %s %s %s %s %s %s" % (self.user_id, self.question,
                                                self.answer, self.date_answer,
                                                self.created, self.modified)

    def __unicode__(self):
        return "%s" % (self.question)


class AppointmentTypes(models.Model):

    """
        AppointmentTypes
    """
    title = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Appointment Types'
        verbose_name_plural = 'Appointment Types'

    def show(self):
        return "Appointment Types %s %s %s" % (self.title,
                                               self.created,
                                               self.modified)

    def __unicode__(self):
        return "%s" % (self.title)


class Appointments(models.Model):

    """
        Appointments
    """
    user = models.ForeignKey(User)
    appointment_types = models.ForeignKey(AppointmentTypes)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    date_appointment = models.DateField(null=True)
    hour_appointment = models.TimeField(null=True)
    recall_one_duration = models.IntegerField(null=True)
    recall_two_duration = models.IntegerField(null=True)
    recall_one_unit = models.IntegerField(null=True)
    recall_two_unit = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Appointments'
        verbose_name_plural = 'Appointments'

    def show(self):
        return "Appointments %s %s %s %s %s" % (self.user_id, self.title,
                                                self.date_appointment,
                                                self.created, self.modified)

    def __unicode__(self):
        return "%s (date: %s)" % (self.title, self.date_appointment)


class Foods(models.Model):

    """
        Foods
    """
    title = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Foods'
        verbose_name_plural = 'Foods'

    def show(self):
        return "Foods %s %s %s" % (self.title, self.created, self.modified)

    def __unicode__(self):
        return "%s" % (self.title)


class Glucoses(models.Model):

    """
        Glucoses
    """
    user = models.ForeignKey(User)
    moment = models.IntegerField(null=True)
    glucose = models.DecimalField(max_digits=5, decimal_places=2)
    insulin = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    comment = models.TextField()
    date_glucose = models.DateField()
    hour_glucose = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Glucose'
        verbose_name_plural = 'Glucoses'

    def show(self):
        return "Glucoses %s %s %s %s %s %s" % (self.user_id, self.moment,
                                               self.glucose, self.insulin,
                                               self.date_glucose,
                                               self.created, self.modified)

    def __unicode__(self):
        return "Glucose: %s Insulin: %s (date: %s)" % (self.glucose, self.insulin, self.date_glucose)


class Meals(models.Model):

    """
        Meals
    """
    user = models.ForeignKey(User)
    food = models.TextField()
    breakfast_lunch_diner = models.CharField(max_length=2)
    date_meal = models.DateField(null=True)
    hour_meal = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'

    def show(self):
        return "Meals %s %s %s %s %s %s" % (self.user_id, self.food,
                                            self.breakfast_lunch_diner,
                                            self.date_meal,
                                            self.created, self.modified)

    def __unicode__(self):
        return "%s (date: %s)" % (self.food, self.date_meal)


class ExaminationTypes(models.Model):

    """
        ExaminationTypes
    """
    title = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Examination Types'
        verbose_name_plural = 'Examination Types'

    def show(self):
        return "Examination Types %s %s %s" % (self.title, self.created,
                                               self.modified)

    def __unicode__(self):
        return "%s" % (self.title)


class Examinations(models.Model):

    """
        Examinations
    """
    user = models.ForeignKey(User)
    examination_types = models.ForeignKey(ExaminationTypes)
    comments = models.TextField()
    date_examination = models.DateField()
    hour_examination = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Examinations'
        verbose_name_plural = 'Examinations'

    def show(self):
        return "Examinations %s %s %s" % (self.examination_types,
                                          self.comments,
                                          self.date_examination,
                                          self.created,
                                          self.modified)

    def __unicode__(self):
        return "%s (date %s) (comment: %s)" % (self.examination_types, self.date_examination, self.comments)


class ExaminationDetails(models.Model):

    """
        ExaminationDetails
    """
    examination = models.ForeignKey(Examinations)
    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=15, decimal_places=5)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Examination Details'
        verbose_name_plural = 'Examination Details'

    def show(self):
        return "Examination Details %s %s %s %s %s" % (self.examination_id,
                                                       self.title,
                                                       self.value,
                                                       self.created,
                                                       self.modified)

    def __unicode__(self):
        return "%s" % (self.title)


class Weights(models.Model):

    """
        Weight
    """
    user = models.ForeignKey(User)
    weight = models.FloatField()
    date_weight = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Weight'
        verbose_name_plural = 'Weights'

    def show(self):
        return "Weights %s %s %s %s %s" % (self.user_id, self.weigth,
                                           self.date_weight,
                                           self.created, self.modified)

    def __unicode__(self):
        return "%s (date: %s)" % (self.weight, self.date_weight)


class Sports(models.Model):

    """
        Sports
    """
    title = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sports'
        verbose_name_plural = 'Sports'

    def show(self):
        return "Sports %s %s %s" % (self.title, self.created, self.modified)

    def __unicode__(self):
        return "%s" % (self.title)


class Exercises(models.Model):

    """
        Exercises
    """
    user = models.ForeignKey(User)
    sports = models.ForeignKey(Sports)
    comment = models.TextField()
    duration = models.FloatField()
    date_exercise = models.DateField(null=True)
    hour_exercise = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def show(self):
        return "Exercises %s %s %s %s %s" % (self.user_id, self.sports,
                                             self.comment, self.created,
                                             self.modified)

    def __unicode__(self):
        return "%s (duration: %s)" % (self.sports, self.duration)


def create_user_profile(sender, instance, created, **kwargs):
    """
        function to create the record in the UserProfile model
    """
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

