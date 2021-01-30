from django.urls import path
from productweb import views

urlpatterns = [
    path("", views.home, name='home'),
    path("detail", views.detail, name='detail'),
]