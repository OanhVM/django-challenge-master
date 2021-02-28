# -*- coding: utf-8 -*-
from django.db.models import Count, Sum
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView
from django.template.defaulttags import register

from mailer.models import Company, Contact


class IndexView(ListView):
    template_name = "mailer/index.html"
    paginate_by = 100

    queryset = Company.objects.prefetch_related("orders") \
        .annotate(order_count=Count("orders")) \
        .annotate(order_sum=Sum("orders__total"))


class CompanyDetailView(ListView):
    template_name = "mailer/company_detail.html"

    def get_queryset(self):
        company_id = self.kwargs.get("id")

        companies_qs = Contact.objects.filter(company_id=company_id).prefetch_related("orders") \
            .annotate(Count("orders")) \
            .annotate(Sum("orders__total"))
        return companies_qs
