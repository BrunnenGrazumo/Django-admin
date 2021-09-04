from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='author').exists()
        return context


class MyView(PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add_post',
                           'simpleapp.change_post')
