#-*- coding: utf-8 -*-
from django.conf.urls import url

from mailer.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
]
