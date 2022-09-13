from django.urls import path
from . import views

urlpatterns = [
    path("habits/", views.HabitListView.as_view(), name="api-habit-list"),
]
