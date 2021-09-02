from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^register$', views.RegisterApi),
    url(r'^register/([0-9]+)$',views.RegisterApi)

]