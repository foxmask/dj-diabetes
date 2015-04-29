# coding: utf-8
from __future__ import unicode_literals
import logging

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView

# dj_diabetes
from dj_diabetes.models import InitMixin, SuccessMixin, PaginateMixin
from dj_diabetes.views import LoginRequiredMixin
from dj_diabetes.models.exams import Examinations
from dj_diabetes.forms.base import ExamsForm, ExamDetailsFormSet

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ExamsMixin(SuccessMixin):
    form_class = ExamsForm
    model = Examinations


class ExamsCreateView(InitMixin, ExamsMixin, LoginRequiredMixin,
                      PaginateMixin, CreateView):
    """
        to Create Exams
    """
    template_name = "dj_diabetes/exams_form.html"

    def form_valid(self, form):
        if self.request.POST:
            formset = ExamDetailsFormSet((self.request.POST or None),
                                         instance=self.object)
            if formset.is_valid():
                self.object = form.save(user=self.request.user)
                formset.instance = self.object
                formset.save()

        else:
            formset = ExamDetailsFormSet(instance=self.object)

        return HttpResponseRedirect(reverse('exams'))

    def get_context_data(self, **kw):
        context = super(ExamsCreateView, self).get_context_data(**kw)
        context['action'] = 'add_exam'

        if self.request.POST:
            context['examsdetails_form'] = ExamDetailsFormSet(self.request.POST)
        else:
            context['examsdetails_form'] = ExamDetailsFormSet(instance=self.object)
        return context


class ExamsUpdateView(ExamsMixin, LoginRequiredMixin,
                      PaginateMixin, UpdateView):
    """
        to Edit Exams
    """
    template_name = "dj_diabetes/exams_form.html"

    def form_valid(self, form):
        formset = ExamDetailsFormSet((self.request.POST or None),
                                     instance=self.object)
        if formset.is_valid():
            self.object = form.save(user=self.request.user)
            formset.instance = self.object
            formset.save()

        return HttpResponseRedirect(reverse('exams'))

    def get_context_data(self, **kw):
        context = super(ExamsUpdateView, self).get_context_data(**kw)

        if self.request.POST:
            context['examsdetails_form'] = ExamDetailsFormSet(self.request.POST)
        else:
            context['examsdetails_form'] = ExamDetailsFormSet(instance=self.object)
        return context


class ExamsDeleteView(ExamsMixin, DeleteView):
    """
        to Delete Examination Details
    """
    template_name = 'dj_diabetes/confirm_delete.html'
