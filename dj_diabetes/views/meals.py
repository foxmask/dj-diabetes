# coding: utf-8
from __future__ import unicode_literals
import logging

from django.views.generic import CreateView, UpdateView, DeleteView

# dj_diabetes
from dj_diabetes.tools import page_it

from dj_diabetes.models import InitMixin, SuccessMixin
from dj_diabetes.views import LoginRequiredMixin
from dj_diabetes.models.meals import Meals
from dj_diabetes.forms.base import MealsForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


class MealsMixin(SuccessMixin):
    form_class = MealsForm
    model = Meals


class MealsCreateView(InitMixin, MealsMixin, LoginRequiredMixin, CreateView):
    """
        to Create Meals
    """
    template_name = "dj_diabetes/meals_form.html"

    def get_form(self, form_class):
        form = super(MealsCreateView, self).get_form(form_class)
        form.instance.user = self.request.user
        return form

    def get_context_data(self, **kw):
        data = Meals.objects.all()
        # paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(MealsCreateView, self).get_context_data(**kw)
        context['action'] = 'add_meal'
        context['data'] = data
        return context


class MealsUpdateView(MealsMixin, LoginRequiredMixin, UpdateView):
    """
        to Edit Meals
    """
    template_name = "dj_diabetes/meals_form.html"

    def get_context_data(self, **kw):
        data = Meals.objects.all()
        # paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(MealsUpdateView, self).get_context_data(**kw)
        context['data'] = data
        return context


class MealsDeleteView(MealsMixin, DeleteView):
    """
        to Delete Meals
    """
    template_name = 'dj_diabetes/confirm_delete.html'
