from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('fetch-stock-prices/', views.fetch_stock_prices, name='fetch_stock_prices'),
]
