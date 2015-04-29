# coding: utf-8
from __future__ import unicode_literals
import logging
import arrow

from django.conf import settings
from django.views.generic import CreateView, UpdateView, DeleteView

# dj_diabetes
from dj_diabetes.tools import page_it

from dj_diabetes.models import SuccessMixin
from dj_diabetes.views import LoginRequiredMixin
from dj_diabetes.models.weights import Weights
from dj_diabetes.forms.base import WeightsForm, UserInstanceMixin

# Get an instance of a logger
logger = logging.getLogger(__name__)


class WeightsMixin(SuccessMixin):
    form_class = WeightsForm
    model = Weights


class WeightsCreateView(WeightsMixin, LoginRequiredMixin, UserInstanceMixin,
                        CreateView):
    """
        to Create Weights
    """
    template_name = "dj_diabetes/weights_form.html"

    def get_initial(self):
        return {'date_weight': arrow.utcnow().to(
            settings.TIME_ZONE).format('YYYY-MM-DD')}

    def get_context_data(self, **kw):
        data = Weights.objects.all()
        # paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(WeightsCreateView, self).get_context_data(**kw)
        context['action'] = 'add_weight'
        context['data'] = data
        return context


class WeightsUpdateView(WeightsMixin, LoginRequiredMixin, UpdateView):
    """
        to Edit Weights
    """
    template_name = "dj_diabetes/weights_form.html"

    def get_context_data(self, **kw):
        data = Weights.objects.all()
        # paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(WeightsUpdateView, self).get_context_data(**kw)
        context['data'] = data
        return context


class WeightsDeleteView(WeightsMixin, DeleteView):
    """
        to Delete Weights
    """
    template_name = 'dj_diabetes/confirm_delete.html'
