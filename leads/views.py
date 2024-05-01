from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import generic


class LandingPageView(generic.TemplateView):
    template_name = "landing_page.html"


class LeadListView(generic.ListView):
    template_name = "leads/leads_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")