#-*- coding: utf-8 -*-
from django.conf.urls import include, url

from mailer.views import IndexView, CompanyDetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^company/(?P<id>\d+)$', CompanyDetailView.as_view(), name="company-detail"),
]
