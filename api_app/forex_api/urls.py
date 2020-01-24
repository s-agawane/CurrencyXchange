from django.urls import path

from .views import get_forex_rate_view

urlpatterns = [
    path(r'', get_forex_rate_view)
    ]