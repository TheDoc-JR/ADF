from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="home"),
    path('register/', views.register_page, name="register_page"),
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logout_user, name="logout_user"),
    path('add_patient/', views.Patients.createPatient, name="new_p"),
    path('find_patient/', views.Patients.fp_page, name="f_p"),
    path('add_tests/', views.AddTests.addTests, name="a_t"),
    path('add_cbc/', views.AddTests.addCBC, name="a_cbc"),
    path('add_bch/', views.AddTests.addBCH, name="a_bch"),
    path('add_enzymes/', views.AddTests.addEnzymes, name="a_enzymes"),
    path('find_tests/', views.ShowTests.ft_page, name="f_t"),
    path('show_cbc/', views.ShowTests.show_cbc, name="show_cbc"),
    path('show_bch/', views.ShowTests.show_bch, name="show_bch"),
    path('show_enzymes/', views.ShowTests.show_enzymes, name="show_enzymes"),
]
