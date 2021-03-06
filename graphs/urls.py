"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import graphs.views as graph_views

urlpatterns = [
    path('upload/', graph_views.upload_data),
    path('search/<str:countryCd>/', graph_views.showDataForCountry),
    path('search/', graph_views.showDataForCountry),
    path('chart/<str:countryCd>', graph_views.data_chart),
    path('chart/', graph_views.data_chart)
]
