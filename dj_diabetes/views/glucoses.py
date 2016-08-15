# coding: utf-8
from __future__ import unicode_literals

import logging

from django.views.generic import CreateView, UpdateView, DeleteView
# dj_diabetes
from dj_diabetes.models import InitMixin, SuccessMixin, PaginateMixin
from dj_diabetes.views import LoginRequiredMixin
from dj_diabetes.models.glucoses import Glucoses
from dj_diabetes.forms.base import GlucosesForm, UserInstanceMixin

# Get an instance of a logger
logger = logging.getLogger(__name__)


class GlucosesMixin(SuccessMixin):
    form_class = GlucosesForm
    model = Glucoses


class GlucosesCreateView(InitMixin, GlucosesMixin, LoginRequiredMixin,
                         UserInstanceMixin, PaginateMixin, CreateView):
    """
        to Create Glucoses
    """
    template_name = "dj_diabetes/glucoses_form.html"


class GlucosesUpdateView(GlucosesMixin, LoginRequiredMixin,
                         PaginateMixin, UpdateView):
    """
        to Edit Glucoses
    """
    template_name = "dj_diabetes/glucoses_form.html"


class GlucosesDeleteView(GlucosesMixin, DeleteView):
    """
        to Delete Glucoses
    """
    template_name = 'dj_diabetes/confirm_delete.html'
