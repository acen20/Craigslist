from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'a'

    def get_queryset(self):
        return "The page is finally Live"
