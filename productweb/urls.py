from django.urls import path
from productweb import views

urlpatterns = [
    path("", views.home, name='home')
]