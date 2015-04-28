# coding: utf-8
from __future__ import unicode_literals
import logging

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView

# dj_diabetes
from dj_diabetes.tools import page_it, right_now
from dj_diabetes.models.sports import Exercises
from dj_diabetes.forms.base import ExercisesForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


#************************
# Classe Based View
#************************


class ExercisesCreateView(CreateView):
    """
        to Create Exercises
    """
    form_class = ExercisesForm
    template_name = "dj_diabetes/exercises_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ExercisesCreateView, self).dispatch(*args, **kwargs)

    def get_initial(self):
        """
            set the default date and hour of the date_xxx and hour_xxx
            property of the current model
        """
        return right_now("exercise")

    def form_valid(self, form):
        exercise = form.save(commit=False)
        if form.is_valid():
            exercise.user = self.request.user
            exercise.save()

        return HttpResponseRedirect(reverse('exercises'))

    def get_context_data(self, **kw):
        data = Exercises.objects.all()
        #paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(ExercisesCreateView, self).get_context_data(**kw)
        context['action'] = 'add_exercise'
        context['data'] = data
        return context


class ExercisesUpdateView(UpdateView):
    """
        to Edit Exercises
    """
    model = Exercises
    form_class = ExercisesForm
    template_name = "dj_diabetes/exercises_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ExercisesUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('exercises'))

    def get_context_data(self, **kw):
        data = Exercises.objects.all()
        #paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(ExercisesUpdateView, self).get_context_data(**kw)
        context['data'] = data
        return context


class ExercisesDeleteView(DeleteView):
    """
        to Delete Exercises
    """
    model = Exercises
    success_url = reverse_lazy('exercises')
    template_name = 'dj_diabetes/confirm_delete.html'
