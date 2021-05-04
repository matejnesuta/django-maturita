from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('produkty', views.ProduktView.as_view(), name='produkty'),
    path('produkty/<int:id>', views.FilteredProduktView.as_view(), name='produkty'),
    path('produkty/detail/<int:pk>', views.ProduktDetailView.as_view(), name='detail')
]
