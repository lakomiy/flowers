from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Assortment

def index(request):
    assortments = Assortment.objects.order_by("-create_at")
    return render(request, "assortment/index.html", {"assortments": assortments})