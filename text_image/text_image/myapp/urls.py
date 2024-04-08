from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('index/', index, name='index'),
    # URL pattern for the main page
    # Add more URL patterns as needed
    path('download-image/', download_image, name='download_image'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
]
