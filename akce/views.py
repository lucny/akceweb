from django.shortcuts import render
from .models import Akce
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

from .forms import AkceForm


def index(request):
    context = {
        'nadpis': 'Web akcí',
        'akce': Akce.objects.order_by('-datum')[2:8],
    }

    return render(request, 'index.html', context=context)

# Doplnit view pro zobrazení seznamu akcí

class AkceDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Akce
    template_name = 'akce_detail.html'
    context_object_name = 'akce'
    permission_required = 'akce.view_akce'
    login_url = "/admin"
    redirect_field_name = 'redirect_to'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["nadpis"] = "Detail akce" 
        return context


class AutorNeboAdminMixin(UserPassesTestMixin):
    def test_func(self):
        akce = self.get_object()
        return self.request.user.is_superuser or akce.autor == self.request.user


class AkceCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Akce
    form_class = AkceForm
    template_name = 'akce_form.html'
    permission_required = 'akce.add_akce'
    login_url = "/admin/login/"

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('akce_detail', kwargs={'pk': self.object.pk})


class AkceUpdateView(PermissionRequiredMixin, LoginRequiredMixin, AutorNeboAdminMixin, UpdateView):
    model = Akce
    form_class = AkceForm
    template_name = 'akce_form.html'
    permission_required = 'akce.change_akce'
    login_url = "/admin/login/"

    def get_success_url(self):
        return reverse('akce_detail', kwargs={'pk': self.object.pk})


class AkceDeleteView(PermissionRequiredMixin, LoginRequiredMixin, AutorNeboAdminMixin, DeleteView):
    model = Akce
    template_name = 'akce_confirm_delete.html'
    permission_required = 'akce.delete_akce'
    success_url = reverse_lazy('akce_list')
    login_url = "/admin/login/"
     