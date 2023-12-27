from django.views.generic import TemplateView, CreateView
from django.http.response import HttpResponseRedirect
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.views import (
	LogoutView,
	PasswordChangeView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _, ngettext_lazy


# HOME
class HomeView(TemplateView):
	template_name = 'common/home.html'

	# REDIRECT IF is_authenticated
	def dispatch(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return HttpResponseRedirect(reverse_lazy('DashboardView'))
		return super().dispatch(*args, **kwargs)


# REGISTER
class RegisterView(CreateView):
	template_name = 'common/register.html'
	form_class = RegisterForm
	success_url = reverse_lazy('DashboardView')


# LOGOUT
class MyLogoutView(LogoutView):
	next_page = reverse_lazy('LoginView')


# CHANGE PASSWORD
class MyPasswordChangeView(PasswordChangeView):
	template_name = 'common/change-password.html'
	success_url = reverse_lazy('MyLogoutView')


# DASHBOARD
class DashboardView(LoginRequiredMixin, TemplateView):
	template_name = 'common/dashboard.html'
	login_url = reverse_lazy('HomeView')
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['page_title'] = _('Dashboard')
		context['page_name'] = _('Dashboard')
		context['dash_active_cls'] = 'active'
		return context


