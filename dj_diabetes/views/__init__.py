# coding: utf-8
import json

from dj_diabetes.forms.base import UserProfileForm
from dj_diabetes.models import UserProfile
from dj_diabetes.models.glucoses import Glucoses

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import UpdateView


def logout_view(request):
    """
        logout the user then redirect him to the home page
    """
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def round_value(value):
    if value:
        return round(float(value), 1)
    else:
        return 0


@login_required
def chart_data_json(request):
    data = {}
    data['chart_data'] = ChartData.get_datas()
    return HttpResponse(json.dumps(data), content_type='application/json')


class ChartData(object):

    @classmethod
    def get_datas(cls):
        glucose_data = Glucoses.objects.all().order_by('-date_glucoses')[:14]

        data = {'date_glucoses': [], 'glucose': []}
        for g in glucose_data:
            data['date_glucoses'].append(g.date_glucoses.strftime('%m/%d'))
            data['glucose'].append(round_value(g.glucose))

        return data


class UserProfileUpdateView(UpdateView):
    """

    """
    model = UserProfile
    form_class = UserProfileForm
    template_name = "dj_diabetes/userprofile_form.html"
    success_url = reverse_lazy('home')


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
