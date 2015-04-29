# coding: utf-8
from __future__ import unicode_literals
import logging

from django.views.generic import CreateView, UpdateView, DeleteView

# dj_diabetes
from dj_diabetes.tools import page_it

from dj_diabetes.models import InitMixin, SuccessMixin
from dj_diabetes.views import LoginRequiredMixin
from dj_diabetes.models.issues import Issues
from dj_diabetes.forms.base import IssuesForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


class IssuesMixin(SuccessMixin):
    form_class = IssuesForm
    model = Issues


class IssuesCreateView(InitMixin, IssuesMixin, LoginRequiredMixin, CreateView):
    """
        to Create Issues
    """
    template_name = "dj_diabetes/issues_form.html"

    def get_form(self, form_class):
        form = super(IssuesCreateView, self).get_form(form_class)
        form.instance.user = self.request.user
        return form

    def get_context_data(self, **kw):
        data = Issues.objects.all().order_by('-created')
        # paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(IssuesCreateView, self).get_context_data(**kw)
        context['action'] = 'add_issue'
        context['data'] = data
        return context


class IssuesUpdateView(IssuesMixin, LoginRequiredMixin, UpdateView):
    """
        to Edit Issues
    """
    template_name = "dj_diabetes/issues_form.html"

    def get_context_data(self, **kw):
        data = Issues.objects.all().order_by('-created')
        # paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(IssuesUpdateView, self).get_context_data(**kw)
        context['data'] = data
        return context


class IssuesDeleteView(IssuesMixin, DeleteView):
    """
        to Delete Issues
    """
    template_name = 'dj_diabetes/confirm_delete.html'
