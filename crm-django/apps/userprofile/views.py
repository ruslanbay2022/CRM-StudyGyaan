from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from apps.userprofile.forms import UserForm, ProfileForm


# Create your views here.

class ProfileView(LoginRequiredMixin, TemplateView):
	template_name = 'profile/profile.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['page_title'] = _('Account Page')
		context['page_name'] = _('Account Page')
		context['profile_active_cls'] = 'active'
		return context


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
	template_name = 'profile/profile-update.html'
	user_form = UserForm
	profile_form = ProfileForm

	def post(self, request):

		post_data = request.POST or None
		file_data = request.FILES or None

		user_form = UserForm(post_data, instance=request.user)
		profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Your profile was successfully updated!')
			return HttpResponseRedirect(reverse_lazy('ProfileView'))

		context = self.get_context_data(
			user_form=user_form,
			profile_form=profile_form,
			# page_title=_('Edit User Page'),
			# page_name=_('Edit User'),
		)

		return self.render_to_response(context)

	# def get(self, request, *args, **kwargs):
	# 	return self.post(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['page_title'] = _('Edit User Page')
		context['page_name'] = _('Edit User')
		context['user_form'] = UserForm(instance=self.request.user)
		context['profile_form'] = ProfileForm(instance=self.request.user.profile)
		return context

