from django.urls import path
from .views import UAVListView, UAVCreateView, UAVUpdateView, UAVDeleteView

urlpatterns = [
    path('', UAVListView.as_view(), name='uav_list'),
    path('add/', UAVCreateView.as_view(), name='uav_add'),
    path('edit/<int:pk>/', UAVUpdateView.as_view(), name='uav_edit'),
    path('delete/<int:pk>/', UAVDeleteView.as_view(), name='uav_delete'),
]
