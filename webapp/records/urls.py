from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="home"),
    path('add_patient/', views.createPatient, name="new_p"),
    path('find_patient/', views.fp_page, name="f_p"),
    path('add_tests/', views.addTests, name="a_t"),
    path('find_tests/', views.ft_page, name="f_t"),
]
