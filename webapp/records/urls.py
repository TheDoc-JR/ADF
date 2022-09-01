from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="home"),
    path('patient/', views.addp_page, name="new_p"),
]
