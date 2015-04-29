# coding: utf-8
from __future__ import unicode_literals
import logging

from django.views.generic import CreateView, UpdateView, DeleteView

# dj_diabetes
from dj_diabetes.tools import page_it

from dj_diabetes.models import InitMixin, SuccessMixin
from dj_diabetes.views import LoginRequiredMixin
from dj_diabetes.models.appointments import Appointments
from dj_diabetes.forms.base import AppointmentsForm, UserInstanceMixin

# Get an instance of a logger
logger = logging.getLogger(__name__)


class AppointmentsMixin(SuccessMixin):
    form_class = AppointmentsForm
    model = Appointments


class AppointmentsCreateView(InitMixin, AppointmentsMixin,
                             LoginRequiredMixin, UserInstanceMixin,
                             CreateView):
    """
        to Create Appointments
    """
    template_name = "dj_diabetes/appointments_form.html"

    def get_context_data(self, **kw):
        data = Appointments.objects.all().order_by('-date_appointments')
        # paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(AppointmentsCreateView, self).get_context_data(**kw)
        context['action'] = 'add_appointments'
        context['data'] = data
        return context


class AppointmentsUpdateView(AppointmentsMixin, LoginRequiredMixin,
                             UpdateView):
    """
        to Edit Appointments
    """
    template_name = "dj_diabetes/appointments_form.html"

    def get_context_data(self, **kw):
        data = Appointments.objects.all().order_by('-date_appointments')
        # paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(AppointmentsUpdateView, self).get_context_data(**kw)
        context['data'] = data
        return context


class AppointmentsDeleteView(AppointmentsMixin, DeleteView):
    """
        to Delete Appointments
    """
    template_name = 'dj_diabetes/confirm_delete.html'
