from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from .models import CRUD
from .forms import CRUDForm


class Home(ListView):
    model = CRUD
    template_name = 'staff/list.html'
    context_object_name = 'staff_members'


class Create(CreateView):
    model = CRUD
    form_class = CRUDForm
    template_name = 'staff/create.html'

    def get_success_url(self):
        return reverse('staff:home')


class Delete(DeleteView):
    model = CRUD
    template_name = 'staff/delete.html'
    context_object_name = 'staff_member'

    def get_success_url(self):
        return reverse('staff:home')


class Detail(DetailView):
    model = CRUD
    template_name = 'staff/detail.html'
    context_object_name = 'staff_member'


class Update(UpdateView):
    model = CRUD
    form_class = CRUDForm
    template_name = 'staff/update.html'

    def get_success_url(self):
        return reverse('staff:detail', kwargs={'pk': self.object.pk})
