# coding: utf-8
import arrow

from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# ************************
# FBV : simple actions   *
# ************************


def page_it(data, record_per_page, page=''):
    """
        return the data of the current page
    """
    paginator = Paginator(data, record_per_page)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999),
        # deliver last page of results.
        data = paginator.page(paginator.num_pages)

    return data


def right_now(model):
    """
        return a dict of 2 property set with current date and time
    """
    now_date = arrow.utcnow().to(settings.TIME_ZONE).format('YYYY-MM-DD')
    now_hour = arrow.utcnow().to(settings.TIME_ZONE).format('HH:mm:ss')
    my_date = 'date_' + model
    my_hour = 'hour_' + model
    return {my_date: now_date, my_hour: now_hour}
