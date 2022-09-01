from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="home"),
    path('add_patient/', views.addp_page, name="new_p"),
    path('find_patient/', views.fp_page, name="f_p"),
    path('add_tests/', views.at_page, name="a_t"),
]
