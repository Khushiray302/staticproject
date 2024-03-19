from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # Define URL pattern for home.html
]