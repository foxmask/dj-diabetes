# coding: utf-8
from __future__ import unicode_literals

import logging

from django.views.generic import CreateView, UpdateView, DeleteView
# dj_diabetes
from dj_diabetes.models import InitMixin, SuccessMixin, PaginateMixin
from dj_diabetes.views import LoginRequiredMixin
from dj_diabetes.models.meals import Meals
from dj_diabetes.forms.base import MealsForm, UserInstanceMixin

# Get an instance of a logger
logger = logging.getLogger(__name__)


class MealsMixin(SuccessMixin):
    form_class = MealsForm
    model = Meals


class MealsCreateView(InitMixin, MealsMixin, LoginRequiredMixin,
                      UserInstanceMixin, PaginateMixin, CreateView):
    """
        to Create Meals
    """
    template_name = "dj_diabetes/meals_form.html"


class MealsUpdateView(MealsMixin, LoginRequiredMixin, PaginateMixin,
                      UpdateView):
    """
        to Edit Meals
    """
    template_name = "dj_diabetes/meals_form.html"


class MealsDeleteView(MealsMixin, DeleteView):
    """
        to Delete Meals
    """
    template_name = 'dj_diabetes/confirm_delete.html'
