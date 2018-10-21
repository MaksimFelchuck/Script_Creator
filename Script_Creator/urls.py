"""Script_Creator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Script.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='Home'),
    path('script/', Script, name='Script'),
    path('scripts/', Scripts, name='Scripts'),
    path('scripts/<str:script_id>/delete', Delete_script, name='Delete_script'),
    path('scripts/edit/<str:script_id>', Edit, name='edit'),
    path('sign-up/', Sign_up, name='Sign-up'),

]
