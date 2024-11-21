from django.urls import path
from . import views

urlpatterns = [  
    path('' ,views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='entre_em_contato'), 

    # captura do item id
    path('item/<int:id>/', views.exibir_item, name='exibir_item'),


]
