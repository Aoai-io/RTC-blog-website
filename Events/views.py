from django.shortcuts import render
from .models import Event
from django.views.generic import ListView, DetailView

# Create your views here.



class EventListView(ListView):
    model = Event
    template_name = "Events/index.html"


class EventDetailView(DetailView):
    model = Event
    template_name = "Events/show.html"
