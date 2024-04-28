from django.urls import path
from . import views

urlpatterns = [
    path('leads/', views.leads_list),
    path('leads/<pk>/', views.lead_detail),
]