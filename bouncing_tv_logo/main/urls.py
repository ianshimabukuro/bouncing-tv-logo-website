# bounce/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL for 'bounce' app maps to 'home' view
]