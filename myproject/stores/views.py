from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

# from stores.models import ########



class IndexView(generic.ListView):
    template_name = "stores/index.html"
