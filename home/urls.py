# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # Página inicial
    path('sobre/', views.sobre, name='sobre'),     # Página sobre
    path('contato/', views.contato, name='contato'),  # Página de contato
]