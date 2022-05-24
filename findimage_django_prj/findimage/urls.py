from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from . import views

urlpatterns = [
    path('dashboard', views.dashboard),
    path('display_table/', views.display_table, name='display_table'),
    path('display_today/', views.display_today, name='display_today'),
    path('display_today_text/', views.display_today_text, name='display_today_text'),
    path('search', views.search, name='search'),

]