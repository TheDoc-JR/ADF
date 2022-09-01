from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('patient/', views.addp_page),
]
