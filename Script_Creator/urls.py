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
from django.urls import path, include
from Script.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', Home, name='Home'),
    path('registration/', RegisterFormView.as_view(), name='registration'),
    path('script/', Script, name='Script'),
    path('gitCreate/', git_clone, name='git'),
    path('scripts/', Scripts, name='Scripts'),
    path('history/', Show_history, name='Show_history'),
    path('scripts/run/<str:script_id>', Run_script, name='Run_script'),
    path('scripts/<str:script_id>/delete', Delete_script, name='Delete_script'),
    path('scripts/edit/<str:script_id>', Edit, name='edit'),


]
