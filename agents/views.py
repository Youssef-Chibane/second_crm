from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent

class AgentListView(LoginRequiredMixin, generic.ListView):
    pass