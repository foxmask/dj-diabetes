# coding: utf-8
from django.contrib import admin

from dj_diabetes.forms import SportsAdminForm, ExaminationTypesAdminForm
from dj_diabetes.forms import AppointmentTypesAdminForm, FoodsAdminForm
from dj_diabetes.forms import PrefAdminForm
from dj_diabetes.models import UserProfile, Preferences
from dj_diabetes.models.foods import Foods
from dj_diabetes.models.sports import Sports
from dj_diabetes.models.exams import ExaminationTypes
from dj_diabetes.models.appointments import AppointmentTypes


class DiabetesAdmin(admin.ModelAdmin):

    list_display = ('title', 'created', 'modified')

    def get_form(self, request, obj=None, **args):
        defaults = {}
        if obj is None:
            defaults.update({'form': self.add_form, })
        else:
            defaults.update({'form': self.view_form, })
        defaults.update(args)
        return super(DiabetesAdmin, self).get_form(request, obj, **defaults)


class SportsAdmin(DiabetesAdmin):

    """
        get the list of the sports
    """
    add_form = SportsAdminForm
    view_form = SportsAdminForm


class FoodsAdmin(admin.ModelAdmin):

    """
        get the list of the Foods
    """
    list_display = ('title', 'created', 'modified')

    add_form = FoodsAdminForm
    view_form = FoodsAdminForm

    def get_form(self, request, obj=None, **args):
        defaults = {}
        if obj is None:
            defaults.update({'form': self.add_form, })
        else:
            defaults.update({'form': self.view_form, })
        defaults.update(args)
        return super(FoodsAdmin, self).get_form(request, obj, **defaults)


class ExaminationTypesAdmin(admin.ModelAdmin):

    """
        get the list of the examination types
    """
    list_display = ('title', 'created', 'modified')

    add_form = ExaminationTypesAdminForm
    view_form = ExaminationTypesAdminForm

    def get_form(self, request, obj=None, **args):
        defaults = {}
        if obj is None:
            defaults.update({'form': self.add_form, })
        else:
            defaults.update({'form': self.view_form, })
        defaults.update(args)
        return super(ExaminationTypesAdmin, self).get_form(request, obj,
                                                           **defaults)


class AppointmentTypesAdmin(admin.ModelAdmin):

    """
        get the list of the appointment types
    """
    list_display = ('title', 'created', 'modified')

    add_form = AppointmentTypesAdminForm
    view_form = AppointmentTypesAdminForm

    def get_form(self, request, obj=None, **args):
        defaults = {}
        if obj is None:
            defaults.update({'form': self.add_form, })
        else:
            defaults.update({'form': self.view_form, })
        defaults.update(args)
        return super(AppointmentTypesAdmin, self).get_form(request, obj,
                                                           **defaults)


class PrefAdmin(admin.ModelAdmin):
    list_display = ('key', 'title', 'value', 'created', 'modified')
    add_form = PrefAdminForm
    view_form = PrefAdminForm

    def get_form(self, request, obj=None, **args):
        defaults = {}
        if obj is None:
            defaults.update({'form': self.add_form, })
        else:
            defaults.update({'form': self.view_form, })
        defaults.update(args)
        return super(PrefAdmin, self).get_form(request, obj, **defaults)


class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'name',)
    list_filter = ['user', 'name']


admin.site.register(Sports, SportsAdmin)
admin.site.register(Foods, FoodsAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(AppointmentTypes, AppointmentTypesAdmin)
admin.site.register(ExaminationTypes, ExaminationTypesAdmin)
admin.site.register(Preferences, PrefAdmin)
