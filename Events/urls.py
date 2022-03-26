from django.urls import path
from .views import EventDetailView, EventListView

urlpatterns = [
    path("", EventListView.as_view(), name="event.index"),
    path("<uuid:pk>/event", EventDetailView.as_view(), name="event.show"),
]
