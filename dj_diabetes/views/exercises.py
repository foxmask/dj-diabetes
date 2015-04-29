# coding: utf-8
from __future__ import unicode_literals
import logging

from django.views.generic import CreateView, UpdateView, DeleteView

# dj_diabetes
from dj_diabetes.tools import page_it

from dj_diabetes.models import InitMixin, SuccessMixin
from dj_diabetes.views import LoginRequiredMixin
from dj_diabetes.models.sports import Exercises
from dj_diabetes.forms.base import ExercisesForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ExercisesMixin(SuccessMixin):
    form_class = ExercisesForm
    model = Exercises


class ExercisesCreateView(InitMixin, ExercisesMixin, LoginRequiredMixin,
                          CreateView):
    """
        to Create Exercises
    """
    template_name = "dj_diabetes/exercises_form.html"

    def get_form(self, form_class):
        form = super(ExercisesCreateView, self).get_form(form_class)
        form.instance.user = self.request.user
        return form

    def get_context_data(self, **kw):
        data = Exercises.objects.all()
        # paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(ExercisesCreateView, self).get_context_data(**kw)
        context['action'] = 'add_exercise'
        context['data'] = data
        return context


class ExercisesUpdateView(ExercisesMixin, LoginRequiredMixin, UpdateView):
    """
        to Edit Exercises
    """
    template_name = "dj_diabetes/exercises_form.html"

    def get_context_data(self, **kw):
        data = Exercises.objects.all()
        # paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(ExercisesUpdateView, self).get_context_data(**kw)
        context['data'] = data
        return context


class ExercisesDeleteView(ExercisesMixin, DeleteView):
    """
        to Delete Exercises
    """
    template_name = 'dj_diabetes/confirm_delete.html'
