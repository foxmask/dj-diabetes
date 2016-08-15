# coding: utf-8
from __future__ import unicode_literals

import logging

import arrow
from django.conf import settings
from django.views.generic import CreateView, UpdateView, DeleteView
# dj_diabetes
from dj_diabetes.models import SuccessMixin, PaginateMixin
from dj_diabetes.views import LoginRequiredMixin
from dj_diabetes.models.weights import Weights
from dj_diabetes.forms.base import WeightsForm, UserInstanceMixin

# Get an instance of a logger
logger = logging.getLogger(__name__)


class WeightsMixin(SuccessMixin):
    form_class = WeightsForm
    model = Weights


class WeightsCreateView(WeightsMixin, LoginRequiredMixin, UserInstanceMixin,
                        PaginateMixin, CreateView):
    """
        to Create Weights
    """
    template_name = "dj_diabetes/weights_form.html"

    def get_initial(self):
        return {'date_weights': arrow.utcnow().to(
            settings.TIME_ZONE).format('YYYY-MM-DD')}


class WeightsUpdateView(WeightsMixin, LoginRequiredMixin,
                        PaginateMixin, UpdateView):
    """
        to Edit Weights
    """
    template_name = "dj_diabetes/weights_form.html"


class WeightsDeleteView(WeightsMixin, DeleteView):
    """
        to Delete Weights
    """
    template_name = 'dj_diabetes/confirm_delete.html'
