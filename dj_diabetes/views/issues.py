# coding: utf-8
from __future__ import unicode_literals
import logging

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView

# dj_diabetes
from dj_diabetes.tools import page_it
from dj_diabetes.models.issues import Issues
from dj_diabetes.forms.base import IssuesForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


#************************
# Classe Based View
#************************


class IssuesCreateView(CreateView):
    """
        to Create Issues
    """
    form_class = IssuesForm
    template_name = "dj_diabetes/issues_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IssuesCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        appointments = form.save(commit=False)
        if form.is_valid():
            appointments.user = self.request.user
            appointments.save()

        return HttpResponseRedirect(reverse('issues'))

    def get_context_data(self, **kw):
        data = Issues.objects.all().order_by('-created')
        #paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(IssuesCreateView, self).get_context_data(**kw)
        context['action'] = 'add_issue'
        context['data'] = data
        return context


class IssuesUpdateView(UpdateView):
    """
        to Edit Issues
    """
    model = Issues
    form_class = IssuesForm
    template_name = "dj_diabetes/issues_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IssuesUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('issues'))

    def get_context_data(self, **kw):
        data = Issues.objects.all().order_by('-created')
        #paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(IssuesUpdateView, self).get_context_data(**kw)
        context['data'] = data
        return context


class IssuesDeleteView(DeleteView):
    """
        to Delete Issues
    """
    model = Issues
    success_url = reverse_lazy('issues')
    template_name = 'dj_diabetes/confirm_delete.html'
