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
from dj_diabetes.models.exams import Examinations, ExaminationTypes
from dj_diabetes.forms.base import ExamsForm, ExamDetailsFormSet

# Get an instance of a logger
logger = logging.getLogger(__name__)


#************************
# Classe Based View
#************************

class ExamsCreateView(CreateView):
    """
        to Create Exams
    """
    form_class = ExamsForm
    template_name = "dj_diabetes/exams_form.html"

    def get_initial(self):
        """
            set the default date and hour of the date_xxx and hour_xxx
            property of the current model
        """
        return right_now("examination")

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
        data = Examinations.objects.all().order_by('-created')
        #paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(ExamsCreateView, self).get_context_data(**kw)
        context['action'] = 'add_exam'
        context['data'] = data

        if self.request.POST:
            context['examsdetails_form'] = ExamDetailsFormSet(self.request.POST)
        else:
            context['examsdetails_form'] = ExamDetailsFormSet(instance=self.object)
        return context


class ExamsUpdateView(UpdateView):
    """
        to Edit Exams
    """
    model = Examinations
    form_class = ExamsForm
    template_name = "dj_diabetes/exams_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ExamsUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        formset = ExamDetailsFormSet((self.request.POST or None),
                                     instance=self.object)
        if formset.is_valid():
            self.object = form.save(user=self.request.user)
            formset.instance = self.object
            formset.save()

        return HttpResponseRedirect(reverse('exams'))

    def get_context_data(self, **kw):
        data = Examinations.objects.all().order_by('-created')
        #paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(ExamsUpdateView, self).get_context_data(**kw)
        context['data'] = data

        if self.request.POST:
            context['examsdetails_form'] = ExamDetailsFormSet(self.request.POST)
        else:
            context['examsdetails_form'] = ExamDetailsFormSet(instance=self.object)
        return context


class ExamsDeleteView(DeleteView):
    """
        to Delete Examination Details
    """
    model = Examinations
    success_url = reverse_lazy('exams')
    template_name = 'dj_diabetes/confirm_delete.html'
