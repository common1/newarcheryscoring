# urls.py
from django.urls import path
from django.contrib import admin

from .views import PersonListView

urlpatterns = [
    path("", PersonListView.as_view())
]