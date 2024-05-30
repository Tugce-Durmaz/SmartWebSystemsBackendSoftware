from django.urls import path
from .views import RentalListView, RentalCreateView, RentalUpdateView, RentalDeleteView

urlpatterns = [
    path('', RentalListView.as_view(), name='rental_list'),
    path('add/', RentalCreateView.as_view(), name='rental_add'),
    path('edit/<int:pk>/', RentalUpdateView.as_view(), name='rental_edit'),
    path('delete/<int:pk>/', RentalDeleteView.as_view(), name='rental_delete'),
]
