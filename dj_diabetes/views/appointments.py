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
from dj_diabetes.models.appointments import Appointments
from dj_diabetes.forms.base import AppointmentsForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


#************************
# Classe Based View
#************************


class AppointmentsCreateView(CreateView):
    """
        to Create Appointments
    """
    form_class = AppointmentsForm
    template_name = "dj_diabetes/appointments_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AppointmentsCreateView, self).dispatch(*args, **kwargs)

    def get_initial(self):
        """
            set the default date and hour of the date_xxx and hour_xxx
            property of the current model
        """
        return right_now("appointment")

    def form_valid(self, form):
        appointments = form.save(commit=False)
        if form.is_valid():
            appointments.user = self.request.user
            appointments.save()

        return HttpResponseRedirect(reverse('appointments'))

    def get_context_data(self, **kw):
        data = Appointments.objects.all().order_by('-date_appointment')
        #paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(AppointmentsCreateView, self).get_context_data(**kw)
        context['action'] = 'add_appointments'
        context['data'] = data
        return context


class AppointmentsUpdateView(UpdateView):
    """
        to Edit Appointments
    """
    model = Appointments
    form_class = AppointmentsForm
    template_name = "dj_diabetes/appointments_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AppointmentsUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('appointments'))

    def get_context_data(self, **kw):
        data = Appointments.objects.all().order_by('-date_appointment')
        #paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(AppointmentsUpdateView, self).get_context_data(**kw)
        context['data'] = data
        return context


class AppointmentsDeleteView(DeleteView):
    """
        to Delete Appointments
    """
    model = Appointments
    success_url = reverse_lazy('appointments')
    template_name = 'dj_diabetes/confirm_delete.html'
