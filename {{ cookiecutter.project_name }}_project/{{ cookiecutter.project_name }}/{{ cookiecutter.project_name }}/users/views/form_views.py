from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.core.exceptions import ImproperlyConfigured
from django.template.loader import render_to_string
from django.contrib.auth import login as auth_login
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse_lazy

from {{ cookiecutter.project_name }}.users.models import CustomUser


class SignOutView(LogoutView):
    pass


class CustomUserSignIn(LoginView):
    template_name = 'snippets/form.j2'
    redirect_url = reverse_lazy('core:redirect')

    def get_redirect_url(self):
        if not self.redirect_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a redirect_url.")
        return str(self.redirect_url)

    def form_invalid(self, form):
        html = render_to_string(self.template_name, self.get_context_data(form=form),
                                request=self.request)
        return HttpResponse(json.dumps({"valid": False, "html": html}),
                            content_type="application/json")

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return HttpResponse(json.dumps({"valid": True}), content_type="application/json")
