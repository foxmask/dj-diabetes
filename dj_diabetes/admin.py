# coding: utf-8
from dj_diabetes.forms import AppointmentTypesAdminForm, FoodsAdminForm
from dj_diabetes.forms import PrefAdminForm
from dj_diabetes.forms import SportsAdminForm, ExaminationTypesAdminForm
from dj_diabetes.models import UserProfile, Preferences
from dj_diabetes.models.appointments import AppointmentTypes
from dj_diabetes.models.exams import ExaminationTypes
from dj_diabetes.models.foods import Foods
from dj_diabetes.models.sports import Sports

from django.contrib import admin


class DiabetesAdminMixin(object):
    list_display = ('title', 'created', 'modified')

    def get_form(self, request, obj=None, **args):
        defaults = {}
        if obj is None:
            defaults.update({'form': self.add_form, })
        else:
            defaults.update({'form': self.view_form, })
        defaults.update(args)
        return super(DiabetesAdminMixin, self).get_form(request, obj,
                                                        **defaults)


class SportsAdmin(DiabetesAdminMixin, admin.ModelAdmin):

    """
        get the list of the sports
    """
    add_form = SportsAdminForm
    view_form = SportsAdminForm


class FoodsAdmin(DiabetesAdminMixin, admin.ModelAdmin):

    """
        get the list of the Foods
    """
    add_form = FoodsAdminForm
    view_form = FoodsAdminForm


class ExaminationTypesAdmin(DiabetesAdminMixin, admin.ModelAdmin):

    """
        get the list of the examination types
    """

    add_form = ExaminationTypesAdminForm
    view_form = ExaminationTypesAdminForm


class AppointmentTypesAdmin(DiabetesAdminMixin, admin.ModelAdmin):

    """
        get the list of the appointment types
    """

    add_form = AppointmentTypesAdminForm
    view_form = AppointmentTypesAdminForm


class PrefAdmin(DiabetesAdminMixin, admin.ModelAdmin):

    list_display = ('key', 'title', 'value', 'created', 'modified')

    add_form = PrefAdminForm
    view_form = PrefAdminForm


class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'name',)
    list_filter = ['user', 'name']


admin.site.register(Sports, SportsAdmin)
admin.site.register(Foods, FoodsAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(AppointmentTypes, AppointmentTypesAdmin)
admin.site.register(ExaminationTypes, ExaminationTypesAdmin)
admin.site.register(Preferences, PrefAdmin)
