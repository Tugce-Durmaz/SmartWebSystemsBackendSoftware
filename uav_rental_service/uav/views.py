from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import UAV
from .forms import UAVForm

class UAVListView(ListView):
    model = UAV
    template_name = 'uav/uav_list.html'

class UAVCreateView(CreateView):
    model = UAV
    form_class = UAVForm
    template_name = 'uav/uav_form.html'
    success_url = reverse_lazy('uav_list')

class UAVUpdateView(UpdateView):
    model = UAV
    form_class = UAVForm
    template_name = 'uav/uav_form.html'
    success_url = reverse_lazy('uav_list')

class UAVDeleteView(DeleteView):
    model = UAV
    template_name = 'uav/uav_confirm_delete.html'
    success_url = reverse_lazy('uav_list')


from django_filters.views import FilterView
from django_filters import rest_framework as filters

class UAVFilter(filters.FilterSet):
    brand = filters.CharFilter(lookup_expr='icontains')
    model = filters.CharFilter(lookup_expr='icontains')
    category = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = UAV
        fields = ['brand', 'model', 'category']

class UAVListView(FilterView):
    model = UAV
    template_name = 'uav/uav_list.html'
    filterset_class = UAVFilter
