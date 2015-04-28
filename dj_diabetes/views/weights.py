# coding: utf-8
from __future__ import unicode_literals
import logging
import arrow

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView

# dj_diabetes
from dj_diabetes.tools import page_it
from dj_diabetes.models.weights import Weights
from dj_diabetes.forms.base import WeightsForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


#************************
# Classe Based View
#************************


class WeightsCreateView(CreateView):
    """
        to Create Weights
    """
    form_class = WeightsForm
    template_name = "dj_diabetes/weights_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WeightsCreateView, self).dispatch(*args, **kwargs)

    def get_initial(self):
        return {'date_weight': arrow.utcnow().to(settings.TIME_ZONE).format('YYYY-MM-DD')}

    def form_valid(self, form):
        weights = form.save(commit=False)
        if form.is_valid():
            weights.user = self.request.user
            weights.save()

        return HttpResponseRedirect(reverse('weights'))

    def get_context_data(self, **kw):
        data = Weights.objects.all()
        #paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(WeightsCreateView, self).get_context_data(**kw)
        context['action'] = 'add_weight'
        context['data'] = data
        return context


class WeightsUpdateView(UpdateView):
    """
        to Edit Weights
    """
    model = Weights
    form_class = WeightsForm
    template_name = "dj_diabetes/weights_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WeightsUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('weights'))

    def get_context_data(self, **kw):
        data = Weights.objects.all()
        #paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(WeightsUpdateView, self).get_context_data(**kw)
        context['data'] = data
        return context


class WeightsDeleteView(DeleteView):
    """
        to Delete Weights
    """
    model = Weights
    success_url = reverse_lazy('weights')
    template_name = 'dj_diabetes/confirm_delete.html'
