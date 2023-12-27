from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from apps.userprofile.forms import UserForm, UserRegisterForm, ProfileForm



# USERS LIST
class UsersListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'editors/editors-home.html'
    model = User
    context_object_name = 'editors'

    def test_func(self):
        curr_us = self.request.user
        if curr_us.is_superuser or curr_us.groups.filter(name='Администраторы').exists():
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _('Editors List')
        context['page_name'] = _('Editors List')
        context['users_active_cls'] = 'active'
        return context


# USER DETAIL
class UsersDetailsView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'editors/editor-details.html'
    model = User
    context_object_name = 'editor'

    def test_func(self):
        curr_us = self.request.user
        if curr_us.is_superuser or curr_us.groups.filter(name='Администраторы').exists():
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = context['page_title'] = 'Editor: ' + self.object.username
        context['users_active_cls'] = 'active'
        return context


# USER UPDATE
class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'editors/editors-update.html'
    user_form = UserForm
    profile_form = ProfileForm

    def test_func(self):
        curr_us = self.request.user
        if curr_us.is_superuser or curr_us.groups.filter(name='Администраторы').exists():
            return True
        return False

    def post(self, request, pk):
        update_user = User.objects.get(id=pk)
        post_data = request.POST or None
        file_data = request.FILES or None
        user_form = UserForm(post_data, instance=update_user)
        profile_form = ProfileForm(post_data, file_data, instance=update_user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse_lazy('UsersDetailsView', kwargs={"pk": self.kwargs['pk']}))
        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form,
        )
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update_user_id = int(self.kwargs['pk'])
        update_user = User.objects.get(id=update_user_id)
        context['editor'] = update_user
        context['page_title'] = _('Edit User Page')
        context['page_name'] = _('Edit User')
        context['user_form'] = UserForm(instance=update_user)
        context['profile_form'] = ProfileForm(instance=update_user.profile)
        context['users_active_cls'] = 'active'
        return context


# CREATE USER
class UserCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'editors/editor-add.html'
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("UsersListView")

    def test_func(self):
        curr_us = self.request.user
        if curr_us.is_superuser or curr_us.groups.filter(name='Администраторы').exists():
            return True
        return False

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _('Add Editor Page')
        context['page_name'] = _('Add Editor')
        context['users_active_cls'] = 'active'
        return context


# DELETE USER
class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy("UsersListView")
    model = User

    def test_func(self):
        curr_us = self.request.user
        if curr_us.is_superuser or curr_us.groups.filter(name='Администраторы').exists():
            return True
        return False

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _('Delete Editor Page')
        context['page_name'] = _('Delete Editor')
        context['users_active_cls'] = 'active'
        return context

