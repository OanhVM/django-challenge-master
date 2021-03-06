# -*- coding: utf-8 -*-
from django.db.models import Count, Sum
from django.template.defaulttags import register
# Create your views here.
from django.views.generic import ListView

from mailer.models import Company, Contact


class IndexView(ListView):
    template_name = "mailer/index.html"
    paginate_by = 100

    queryset = Company.objects.prefetch_related("orders") \
        .annotate(order_count=Count("orders")) \
        .annotate(order_sum=Sum("orders__total")) \
        .values()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        companies = context["company_list"]
        company_ids = [company["id"] for company in companies]

        contacts_qs = Contact.objects.prefetch_related("orders") \
            .annotate(order_count=Count("orders")) \
            .annotate(order_sum=Sum("orders__total")) \
            .filter(company_id__in=company_ids) \
            .values()

        company_dic = {}
        for company in companies:
            company_dic[company["id"]] = [contact for contact in contacts_qs if contact["company_id"] == company["id"]]

        context["contacts_per_company"] = company_dic
        return context


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
