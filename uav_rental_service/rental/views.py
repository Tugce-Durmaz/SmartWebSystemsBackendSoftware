from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Rental
from .forms import RentalForm
class RentalListView(ListView):
    model = Rental
    template_name = 'rental/rental_list.html'

class RentalCreateView(CreateView):
    model = Rental
    form_class = RentalForm
    template_name = 'rental/rental_form.html'
    success_url = reverse_lazy('rental_list')

class RentalUpdateView(UpdateView):
    model = Rental
    form_class = RentalForm
    template_name = 'rental/rental_form.html'
    success_url = reverse_lazy('rental_list')

class RentalDeleteView(DeleteView):
    model = Rental
    template_name = 'rental/rental_confirm_delete.html'
    success_url = reverse_lazy('rental_list')
