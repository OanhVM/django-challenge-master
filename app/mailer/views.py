#-*- coding: utf-8 -*-
from django.db.models import Count, Sum
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView

from mailer.models import Company


class IndexView(ListView):
    template_name = "mailer/index.html"
    paginate_by = 100

    queryset = Company.objects.prefetch_related("contacts", "orders") \
        .annotate(order_count=Count("orders")) \
        .annotate(order_sum=Sum("orders__total"))
