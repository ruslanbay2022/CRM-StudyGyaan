from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from .models import Child
from .forms import ChildForm
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _


# CHILD LIST HOME
class ChildrenView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'children/children-home.html'
    model = Child
    queryset = Child.objects.filter(archived=False)
    context_object_name = 'children'

    def test_func(self):
        curr_us = self.request.user
        if curr_us.is_superuser or curr_us.groups.filter(name='Редакторы детей').exists():
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _('Children List')
        context['page_name'] = _('Children List')
        context['children_active_cls'] = 'active'
        # context['children'] = Child.objects.all()
        return context


# ARCHIVED CHILD LIST HOME
class ChildrenArchivedView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'children/children-home.html'
    model = Child
    queryset = Child.objects.filter(archived=True)
    context_object_name = 'children'

    def test_func(self):
        curr_us = self.request.user
        if curr_us.is_superuser or curr_us.groups.filter(name='Редакторы детей').exists():
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _('Archive Children List')
        context['page_name'] = _('Archive Children List')
        context['children_active_cls'] = 'active'
        return context


# GIRLS LIST
class GirlsView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'children/children-home.html'
    model = Child
    filter_args = {'gender': 'W', 'archived': 'False'}
    queryset = Child.objects.filter(**filter_args)
    context_object_name = 'children'

    def test_func(self):
        curr_us = self.request.user
        if curr_us.is_superuser or curr_us.groups.filter(name='Редакторы детей').exists():
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _('Girls List')
        context['page_name'] = _('Girls List')
        context['children_active_cls'] = 'active'
        return context


# BOYS LIST
class BoysView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'children/children-home.html'
    model = Child
    # queryset = Child.objects.filter(gender='M')
    filter_args = {'gender': 'M', 'archived': 'False'}
    queryset = Child.objects.filter(**filter_args)
    context_object_name = 'children'

    def test_func(self):
        curr_us = self.request.user
        if curr_us.is_superuser or curr_us.groups.filter(name='Редакторы детей').exists():
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _('Boys List')
        context['page_name'] = _('Boys List')
        context['children_active_cls'] = 'active'
        return context


# CHILD DETAIL
class ChildDetailsView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'children/child-details.html'
    model = Child
    context_object_name = 'child'

    def test_func(self):
        curr_us = self.request.user
        if curr_us.is_superuser or curr_us.groups.filter(name='Редакторы детей').exists():
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = context['page_title'] = self.object.name + ' ' + self.object.middlename + ' ' + self.object.surname
        context['children_active_cls'] = 'active'
        return context


# CHILD UPDATE
class ChildUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'children/child-update.html'
    model = Child
    form_class = ChildForm

    def test_func(self):
        curr_us = self.request.user
        if curr_us.is_superuser or curr_us.groups.filter(name='Редакторы детей').exists():
            return True
        return False

    def get_success_url(self):
        return reverse(
            "ChildDetailsView",
            kwargs={"pk": self.object.pk}
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _('Update Product') + ' ' + self.object.name
        context['page_name'] = _('Update Product') + ' ' + self.object.name
        context['children_active_cls'] = 'active'
        context['back_link'] = True
        return context


# CREATE CHILD
class ChildCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'children/child-add.html'
    model = Child
    form_class = ChildForm
    success_url = reverse_lazy("ChildrenView")

    def test_func(self):
        curr_us = self.request.user
        if curr_us.is_superuser or curr_us.groups.filter(name='Редакторы детей').exists():
            return True
        return False

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _('Add Child Page')
        context['page_name'] = _('Add Child')
        context['children_active_cls'] = 'active'
        return context


# DELETE CHILD
class ChildDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy("ChildrenView")
    model = Child

    def test_func(self):
        curr_us = self.request.user
        if curr_us.is_superuser or curr_us.groups.filter(name='Редакторы детей').exists():
            return True
        return False

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _('Delete Child Page')
        context['page_name'] = _('Delete Child')
        context['children_active_cls'] = 'active'
        return context
