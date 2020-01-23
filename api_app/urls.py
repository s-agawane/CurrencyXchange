from django.urls import path

from .views import show_balance_view, deposit_balance_view, withdraw_balance_view

urlpatterns = [
    path('view/', show_balance_view),
    path('deposit/', deposit_balance_view),
    path('withdraw/', withdraw_balance_view),
    ]


