from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="home"),
    path('add_patient/', views.createPatient, name="new_p"),
    path('find_patient/', views.fp_page, name="f_p"),
    path('add_tests/', views.addTests, name="a_t"),
    path('add_cbc/', views.addCBC, name="a_cbc"),
    path('add_bch/', views.addBCH, name="a_bch"),
    path('add_enzymes/', views.addEnzymes, name="a_enzymes"),
    path('find_tests/', views.ft_page, name="f_t"),
    path('show_cbc/', views.show_cbc, name="show_cbc"),
    path('show_bch/', views.show_bch, name="show_bch"),
    path('show_enzymes/', views.show_enzymes, name="show_enzymes"),
]
