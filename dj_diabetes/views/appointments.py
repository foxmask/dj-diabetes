# coding: utf-8
from __future__ import unicode_literals

import logging

from django.views.generic import CreateView, UpdateView, DeleteView
# dj_diabetes
from dj_diabetes.models import InitMixin, SuccessMixin, PaginateMixin
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
                             PaginateMixin, CreateView):
    """
        to Create Appointments
    """
    template_name = "dj_diabetes/appointments_form.html"


class AppointmentsUpdateView(AppointmentsMixin, LoginRequiredMixin,
                             PaginateMixin, UpdateView):
    """
        to Edit Appointments
    """
    template_name = "dj_diabetes/appointments_form.html"


class AppointmentsDeleteView(AppointmentsMixin, DeleteView):
    """
        to Delete Appointments
    """
    template_name = 'dj_diabetes/confirm_delete.html'
