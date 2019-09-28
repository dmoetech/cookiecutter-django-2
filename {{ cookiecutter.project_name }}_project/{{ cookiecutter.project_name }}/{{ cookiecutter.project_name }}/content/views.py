from django.shortcuts import render

from {{ cookiecutter.project_name }}.core.views import WebsiteView


# Create your views here.
class IndexView(WebsiteView):
    template_name = 'index.html'
