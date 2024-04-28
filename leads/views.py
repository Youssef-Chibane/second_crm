from django.shortcuts import render
from django.http import HttpResponse


def leads_list(request):
    # return HttpResponse("Hello World")
    return render(request, 'leads_list.html')