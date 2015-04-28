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
from dj_diabetes.models.meals import Meals
from dj_diabetes.forms.base import MealsForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


class MealsCreateView(CreateView):
    """
        to Create Meals
    """
    form_class = MealsForm
    template_name = "dj_diabetes/meals_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MealsCreateView, self).dispatch(*args, **kwargs)

    def get_initial(self):
        """
            set the default date and hour of the date_xxx and hour_xxx
            property of the current model
        """
        return right_now("meal")

    def form_valid(self, form):
        meals = form.save(commit=False)
        if form.is_valid():
            meals.user = self.request.user
            meals.save()

        return HttpResponseRedirect(reverse('meals'))

    def get_context_data(self, **kw):
        data = Meals.objects.all()
        #paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(MealsCreateView, self).get_context_data(**kw)
        context['action'] = 'add_meal'
        context['data'] = data
        return context


class MealsUpdateView(UpdateView):
    """
        to Edit Meals
    """
    model = Meals
    form_class = MealsForm
    template_name = "dj_diabetes/meals_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MealsUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('meals'))

    def get_context_data(self, **kw):
        data = Meals.objects.all()
        #paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(MealsUpdateView, self).get_context_data(**kw)
        context['data'] = data
        return context


class MealsDeleteView(DeleteView):
    """
        to Delete Meals
    """
    model = Meals
    success_url = reverse_lazy('meals')
    template_name = 'dj_diabetes/confirm_delete.html'
