
from django.contrib import admin
from django.urls import path
from . import views

app_name='mutliuserauth'

urlpatterns = [
   
    path('', views.login ,name='login'),
    path('logout', views.logoutuser ,name='logoutuser'),
    path('admin-dashboard/', views.admin_dashboard ,name='admin_dashboard'),
    path('agent_register/', views.agent_register ,name='agent_register'),
    path('agent_dashboard/', views.agent_dashboard ,name='agent_dashboard'),
    path('customer_dashboard/', views.customer_dashboard ,name='customer_dashboard'),
]
