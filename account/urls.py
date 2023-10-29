from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login),
    path('logout', views.user_logout),
]
