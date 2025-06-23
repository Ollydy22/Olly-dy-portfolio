
from django.urls import path
from . import views

urlpatterns = [
    # This maps the root URL ('') to our home_view function in views.py
    path('', views.home_view, name='home'),
]
