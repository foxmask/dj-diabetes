# coding: utf-8
from __future__ import unicode_literals
import logging

from django.views.generic import CreateView, UpdateView, DeleteView

# dj_diabetes
from dj_diabetes.tools import page_it

from dj_diabetes.models import InitMixin, SuccessMixin
from dj_diabetes.views import LoginRequiredMixin
from dj_diabetes.models.glucoses import Glucoses
from dj_diabetes.forms.base import GlucosesForm, UserInstanceMixin

# Get an instance of a logger
logger = logging.getLogger(__name__)


class GlucosesMixin(SuccessMixin):
    form_class = GlucosesForm
    model = Glucoses


class GlucosesCreateView(InitMixin, GlucosesMixin, LoginRequiredMixin,
                         UserInstanceMixin, CreateView):
    """
        to Create Glucoses
    """
    template_name = "dj_diabetes/glucoses_form.html"

    def get_context_data(self, **kw):
        data = Glucoses.objects.all().order_by('-date_glucoses')
        # paginator vars
        record_per_page = 5
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(GlucosesCreateView, self).get_context_data(**kw)
        context['action'] = 'add_glucoses'
        context['data'] = data
        return context


class GlucosesUpdateView(GlucosesMixin, LoginRequiredMixin,
                         UpdateView):
    """
        to Edit Glucoses
    """
    template_name = "dj_diabetes/glucoses_form.html"

    def get_context_data(self, **kw):
        data = Glucoses.objects.all().order_by('-date_glucoses')
        # paginator vars
        record_per_page = 5
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(GlucosesUpdateView, self).get_context_data(**kw)
        context['data'] = data
        return context


class GlucosesDeleteView(GlucosesMixin, DeleteView):
    """
        to Delete Glucoses
    """
    template_name = 'dj_diabetes/confirm_delete.html'
