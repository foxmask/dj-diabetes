# coding: utf-8
from __future__ import unicode_literals

import logging

import arrow
from django.conf import settings
from django.views.generic import CreateView, UpdateView, DeleteView
# dj_diabetes
from dj_diabetes.models import InitMixin, SuccessMixin, PaginateMixin
from dj_diabetes.views import LoginRequiredMixin
from dj_diabetes.models.issues import Issues
from dj_diabetes.forms.base import IssuesForm, UserInstanceMixin

# Get an instance of a logger
logger = logging.getLogger(__name__)


class IssuesMixin(SuccessMixin):
    form_class = IssuesForm
    model = Issues


class IssuesCreateView(InitMixin, IssuesMixin, LoginRequiredMixin,
                       PaginateMixin, UserInstanceMixin, CreateView):
    """
        to Create Issues
    """
    template_name = "dj_diabetes/issues_form.html"

    def get_initial(self):
        return {'date_answer': arrow.utcnow().to(
            settings.TIME_ZONE).format('YYYY-MM-DD')}


class IssuesUpdateView(IssuesMixin, LoginRequiredMixin, PaginateMixin,
                       UpdateView):
    """
        to Edit Issues
    """
    template_name = "dj_diabetes/issues_form.html"


class IssuesDeleteView(IssuesMixin, DeleteView):
    """
        to Delete Issues
    """
    template_name = 'dj_diabetes/confirm_delete.html'
