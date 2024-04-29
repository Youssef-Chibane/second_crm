from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def landing_page(request):
    return render(request, 'landing_page.html')


def leads_list(request):
    # return HttpResponse("Hello World")
    leads = Lead.objects.all()
    return render(request, 'leads/leads_list.html', {"leads": leads})


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    return render(request, 'leads/lead_detail.html', {"lead": lead})


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    return render(request, "leads/lead_create.html", {"form": form})


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    return render(request, 'leads/lead_update.html', {"form": form, "lead": lead})


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")