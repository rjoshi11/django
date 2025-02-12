from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),  # Added '' for root URL and corrected the path
    path('about/', views.about, name='about'), # added trailing slash
    path('services/', views.services, name='services'), # added trailing slash
    path('contact/', views.contact, name='contact'), # added trailing slash
    path('admin/', admin.site.urls), # Keep the admin url
]