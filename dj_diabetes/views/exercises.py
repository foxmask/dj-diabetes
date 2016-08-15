# coding: utf-8
from __future__ import unicode_literals

import logging

from django.views.generic import CreateView, UpdateView, DeleteView
# dj_diabetes
from dj_diabetes.models import InitMixin, SuccessMixin, PaginateMixin
from dj_diabetes.views import LoginRequiredMixin
from dj_diabetes.models.sports import Exercises
from dj_diabetes.forms.base import ExercisesForm, UserInstanceMixin

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ExercisesMixin(SuccessMixin):
    form_class = ExercisesForm
    model = Exercises


class ExercisesCreateView(InitMixin, ExercisesMixin, LoginRequiredMixin,
                          UserInstanceMixin, PaginateMixin, CreateView):
    """
        to Create Exercises
    """
    template_name = "dj_diabetes/exercises_form.html"


class ExercisesUpdateView(ExercisesMixin, LoginRequiredMixin,
                          PaginateMixin, UpdateView):
    """
        to Edit Exercises
    """
    template_name = "dj_diabetes/exercises_form.html"


class ExercisesDeleteView(ExercisesMixin, DeleteView):
    """
        to Delete Exercises
    """
    template_name = 'dj_diabetes/confirm_delete.html'
