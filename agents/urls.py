from django.urls import path
from .views import *

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agent-list'),
]