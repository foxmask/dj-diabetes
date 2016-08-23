# coding: utf-8
from dj_diabetes.tools import page_it, right_now

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.views.generic.edit import ModelFormMixin


class HatModel(models.Model):
    """
        HatModel
    """
    title = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % self.title


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

    def __str__(self):
        return "%s" % self.user


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

    def __str__(self):
        return "%s %s %s" % (self.key, self.title, self.value)


def create_user_profile(sender, instance, created, **kwargs):
    """
        function to create the record in the UserProfile model
    """
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


"""
    Common mixin for all models of the app
"""


class InitMixin(ModelFormMixin):
    """
        Mixin to initialize the date/hour attribute of the model
    """
    def get_initial(self):
        """
            set the default date and hour of the date_xxx and hour_xxx
            property of the current model
        """
        return right_now(self.model.__name__.lower())


class SuccessMixin(object):
    """
        Mixin to just return to the expected page
        where the name is based on the model name
    """
    def get_success_url(self):
        return reverse(self.model.__name__.lower())


class PaginateMixin(object):
    """
        Mixin to just handle the Paginate behavior
    """
    def get_context_data(self, **kw):
        data = self.model.objects.all()
        # paginator vars
        record_per_page = 3
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)
        context = super(PaginateMixin, self).get_context_data(**kw)
        context['data'] = data
        return context
