from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('sobre/', views.sobre, name='sobre'),  
    path('contato/', views.contato, name='contato'), 
    path('diasemana/<int:dia>/', views.dia_da_semana, name='dia_da_semana'),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
]
