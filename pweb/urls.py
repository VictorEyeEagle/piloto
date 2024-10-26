# pweb/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para o admin
    path('', include('home.urls')),  # Incluir as URLs da app home
]
