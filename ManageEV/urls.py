"""
URL configuration for ManageEV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_UserAdmin/', include('api_UserAdmin.urls')),
    path('api_Route/', include('api_Route.urls')),
    path('api_ChargePoint/', include('api_ChargePoint.urls')),
    path('api_ElectricVehicle/', include('api_ElectricVehicle.urls')),
    path('docs_UserAdmin/', include_docs_urls(title = 'Api User Admin Documentation')),
    path('docs_Route/', include_docs_urls(title = 'Api Route Documentation')),
    path('docs_ChargePoint/', include_docs_urls(title = 'Api Charge Point Documentation')),
    path('docs_ElectricVehicle/', include_docs_urls(title = 'Api Electric Vehicle Documentation')),
    path('api_Model/', include('api_Model.urls')),
    path('api_Trip/', include('api_Trip.urls')),
    path('docs_Trip/', include_docs_urls(title = 'Api Trip Documentation')),
    path('api_Statistics_percentage/', include('api_Statistics_percentage.urls')),
    path('docs_Statistics_percentage/', include_docs_urls(title = 'Api Statistics Percentage Documentation')),
    path('api_Statistics_consumption/', include('api_Statistics_consumption.urls')),
    path('docs_Statistics_consumption/', include_docs_urls(title = 'Api Statistics Consumption Documentation')),
]
