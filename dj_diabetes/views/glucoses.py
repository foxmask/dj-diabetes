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
from dj_diabetes.models.glucoses import Glucoses
from dj_diabetes.forms.base import GlucosesForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


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

    def get_initial(self):
        """
            set the default date and hour of the date_xxx and hour_xxx
            property of the current model
        """
        return right_now("glucose")

    def form_valid(self, form):
        glucose = form.save(commit=False)
        if form.is_valid():
            glucose.user = self.request.user
            glucose.save()

        return HttpResponseRedirect(reverse('home'))

    def get_context_data(self, **kw):
        data = Glucoses.objects.all().order_by('-date_glucose')
        #paginator vars
        record_per_page = 5
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

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
    form_class = GlucosesForm
    template_name = "dj_diabetes/glucoses_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GlucosesUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('home'))

    def get_context_data(self, **kw):
        data = Glucoses.objects.all().order_by('-date_glucose')
        #paginator vars
        record_per_page = 5
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(GlucosesUpdateView, self).get_context_data(**kw)
        context['data'] = data
        return context


class GlucosesDeleteView(DeleteView):
    """
        to Delete Glucoses
    """
    model = Glucoses
    success_url = reverse_lazy('home')
    template_name = 'dj_diabetes/confirm_delete.html'
