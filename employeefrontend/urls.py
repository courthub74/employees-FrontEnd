from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_home, name="login"),
    path('main/', views.main, name="main"),
]
