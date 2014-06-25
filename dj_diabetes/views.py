# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import logging

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView

# dj_diabetes
from dj_diabetes.models import Appointments, Examinations, ExaminationDetails
from dj_diabetes.models import Issues, Exercises, Glucoses, Weights, Meals
from dj_diabetes.forms import GlucosesForm, AppointmentsForm, IssuesForm
from dj_diabetes.forms import WeightsForm, MealsForm, ExercisesForm, ExamsForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


#************************
# FBV : simple actions  *
#************************

def logout_view(request):
    """
        logout the user then redirect him to the home page
    """
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def round_value(value):
    if value:
        return round(float(value), 1)
    else:
        return 0


@login_required
def chart_data_json(request):
    data = {}
    data['chart_data'] = ChartData.get_datas()
    return HttpResponse(json.dumps(data), content_type='application/json')


class ChartData(object):

    @classmethod
    def get_datas(cls):
        glucose_data = Glucoses.objects.all().order_by('-date_glucose')[:14]

        data = {'date_glucose': [], 'glucose': []}
        for g in glucose_data:
            data['date_glucose'].append(g.date_glucose.strftime('%m/%d'))
            data['glucose'].append(round_value(g.glucose))

        return data

#************************
# Classe Based View
#************************


class GlucosesCreateView(CreateView):
    """
        to Create Glucoses
    """
    form_class = GlucosesForm
    template_name = "dj_diabetes/glucoses_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GlucosesCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        glucose = form.save(commit=False)
        if form.is_valid():
            glucose.user = self.request.user
            glucose.save()

        return HttpResponseRedirect(reverse('home'))

    def get_context_data(self, **kw):
        data = Glucoses.objects.all().order_by('-date_glucose')[:14]

        context = super(GlucosesCreateView, self).get_context_data(**kw)
        #context['use_insuline'] = [False if insulin in GlucosesForm]
        context['action'] = 'add_glucoses'
        context['data'] = data
        return context


class GlucosesUpdateView(UpdateView):
    """
        to Edit Glucoses
    """
    model = Glucoses
    template_name = "dj_diabetes/glucoses_form.html"
    fields = ['moment', 'comment', 'glucose', 'insulin', 'date_glucose']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GlucosesUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('home'))

    def get_context_data(self, **kw):
        context = super(GlucosesUpdateView, self).get_context_data(**kw)
        context['data'] = Glucoses.objects.all()
        return context


class GlucosesDeleteView(DeleteView):
    """
        to Delete Glucoses
    """
    model = Glucoses
    success_url = reverse_lazy('home')
    template_name = 'dj_diabetes/confirm_delete.html'


class AppointmentsCreateView(CreateView):
    """
        to Create Appointments
    """
    form_class = AppointmentsForm
    template_name = "dj_diabetes/appointments_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AppointmentsCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        appointments = form.save(commit=False)
        if form.is_valid():
            appointments.user = self.request.user
            appointments.save()

        return HttpResponseRedirect(reverse('appointments'))

    def get_context_data(self, **kw):
        context = super(AppointmentsCreateView, self).get_context_data(**kw)
        context['action'] = 'add_appointments'
        context['data'] = Appointments.objects.all()
        return context


class AppointmentsUpdateView(UpdateView):
    """
        to Edit Appointments
    """
    model = Appointments
    template_name = "dj_diabetes/appointments_form.html"
    fields = ['appointment_types', 'title', 'body', 'date_appointment',
              'recall_one_duration', 'recall_two_duration',
              'recall_one_unit', 'recall_two_unit']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AppointmentsUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('appointments'))

    def get_context_data(self, **kw):
        context = super(AppointmentsUpdateView, self).get_context_data(**kw)
        context['data'] = Appointments.objects.all()
        return context


class AppointmentsDeleteView(DeleteView):
    """
        to Delete Appointments
    """
    model = Appointments
    success_url = reverse_lazy('appointments')
    template_name = 'dj_diabetes/confirm_delete.html'


class IssuesCreateView(CreateView):
    """
        to Create Issues
    """
    form_class = IssuesForm
    template_name = "dj_diabetes/issues_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IssuesCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        appointments = form.save(commit=False)
        if form.is_valid():
            appointments.user = self.request.user
            appointments.save()

        return HttpResponseRedirect(reverse('issues'))

    def get_context_data(self, **kw):
        context = super(IssuesCreateView, self).get_context_data(**kw)
        context['action'] = 'add_issue'
        context['data'] = Issues.objects.all()
        return context


class IssuesUpdateView(UpdateView):
    """
        to Edit Issues
    """
    model = Issues
    fields = ['question', 'question_to', 'answer', 'date_answer']
    template_name = "dj_diabetes/issues_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IssuesUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('issues'))

    def get_context_data(self, **kw):
        context = super(IssuesUpdateView, self).get_context_data(**kw)
        context['data'] = Issues.objects.all()
        return context


class IssuesDeleteView(DeleteView):
    """
        to Delete Issues
    """
    model = Issues
    success_url = reverse_lazy('issues')
    template_name = 'dj_diabetes/confirm_delete.html'


class WeightsCreateView(CreateView):
    """
        to Create Weights
    """
    form_class = WeightsForm
    template_name = "dj_diabetes/weights_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WeightsCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        weights = form.save(commit=False)
        if form.is_valid():
            weights.user = self.request.user
            weights.save()

        return HttpResponseRedirect(reverse('weights'))

    def get_context_data(self, **kw):
        context = super(WeightsCreateView, self).get_context_data(**kw)
        context['action'] = 'add_weight'
        context['data'] = Weights.objects.all()
        return context


class WeightsUpdateView(UpdateView):
    """
        to Edit Weights
    """
    model = Weights
    fields = ['weight', 'date_weight']
    template_name = "dj_diabetes/weights_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WeightsUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('weights'))

    def get_context_data(self, **kw):
        context = super(WeightsUpdateView, self).get_context_data(**kw)
        context['data'] = Weights.objects.all()
        return context


class WeightsDeleteView(DeleteView):
    """
        to Delete Weights
    """
    model = Weights
    success_url = reverse_lazy('weight')
    template_name = 'dj_diabetes/confirm_delete.html'


class MealsCreateView(CreateView):
    """
        to Create Meals
    """
    form_class = MealsForm
    template_name = "dj_diabetes/meals_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MealsCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        meals = form.save(commit=False)
        print "meals ? ", meals.breakfast_lunch_diner
        print type(meals.breakfast_lunch_diner)
        if form.is_valid():
            meals.user = self.request.user
            meals.save()

        return HttpResponseRedirect(reverse('meals'))

    def get_context_data(self, **kw):
        context = super(MealsCreateView, self).get_context_data(**kw)
        context['action'] = 'add_meal'
        context['data'] = Meals.objects.all()
        return context


class MealsUpdateView(UpdateView):
    """
        to Edit Meals
    """
    model = Meals
    fields = ['food', 'breakfast_lunch_diner', 'meal_date']
    template_name = "dj_diabetes/meals_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MealsUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('meals'))

    def get_context_data(self, **kw):
        context = super(MealsUpdateView, self).get_context_data(**kw)
        context['data'] = Meals.objects.all()
        return context


class MealsDeleteView(DeleteView):
    """
        to Delete Meals
    """
    model = Meals
    success_url = reverse_lazy('meals')
    template_name = 'dj_diabetes/confirm_delete.html'


class ExercisesCreateView(CreateView):
    """
        to Create Exercises
    """
    form_class = ExercisesForm
    template_name = "dj_diabetes/exercises_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ExercisesCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        exercise = form.save(commit=False)
        if form.is_valid():
            exercise.user = self.request.user
            exercise.save()

        return HttpResponseRedirect(reverse('exercises'))

    def get_context_data(self, **kw):
        context = super(ExercisesCreateView, self).get_context_data(**kw)
        context['action'] = 'add_exercise'
        context['data'] = Exercises.objects.all()
        return context


class ExercisesUpdateView(UpdateView):
    """
        to Edit Exercises
    """
    model = Exercises
    fields = fields = ['sports', 'comment', 'duration', 'date_exercise']
    template_name = "dj_diabetes/exercises_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ExercisesUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('exercises'))

    def get_context_data(self, **kw):
        context = super(ExercisesUpdateView, self).get_context_data(**kw)
        context['data'] = Exercises.objects.all()
        return context


class ExercisesDeleteView(DeleteView):
    """
        to Delete Exercises
    """
    model = Exercises
    success_url = reverse_lazy('exercises')
    template_name = 'dj_diabetes/confirm_delete.html'


class ExamsCreateView(CreateView):
    """
        to Create Exams
    """
    form_class = ExamsForm
    template_name = "dj_diabetes/exams_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ExamsCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        exercise = form.save(commit=False)
        if form.is_valid():
            exercise.user = self.request.user
            exercise.save()

        return HttpResponseRedirect(reverse('exams'))

    def get_context_data(self, **kw):
        context = super(ExamsCreateView, self).get_context_data(**kw)
        context['action'] = 'add_exam'
        context['data'] = Examinations.objects.all()
        return context


class ExamsUpdateView(UpdateView):
    """
        to Edit Exams
    """
    model = Examinations

    #from django.forms.models import modelformset_factory
    #ExaminationDetailsFormSet = modelformset_factory(ExaminationDetails, extra=1)

    fields = ['examination_types', 'comments', 'date_examination']
    template_name = "dj_diabetes/exams_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ExamsUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('exams'))

    def get_context_data(self, **kw):
        context = super(ExamsUpdateView, self).get_context_data(**kw)
        context['data'] = Examinations.objects.all()
        # context['formset'] = self.ExaminationDetailsFormSet()
        return context


class ExamsDeleteView(DeleteView):
    """
        to Delete Examination Details
    """
    model = Examinations
    success_url = reverse_lazy('exams')
    template_name = 'dj_diabetes/confirm_delete.html'
