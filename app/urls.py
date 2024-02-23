from django.urls import path

from . import views

urlpatterns = [
    path('menus/', views.home, name='home'),
]
