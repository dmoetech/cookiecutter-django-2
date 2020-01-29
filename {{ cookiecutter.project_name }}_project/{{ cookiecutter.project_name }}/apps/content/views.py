from django.views.generic import TemplateView
from django.shortcuts import render

from apps.core.views import WebsiteContextMixin


class IndexView(WebsiteContextMixin, TemplateView):
    template_name = 'index.html'
