from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('api_Route/', include('api_Route.urls')),
    # path('api_ChargePoint/', include('api_ChargePoint.urls')),
    # path('api_ElectricVehicle/', include('api_ElectricVehicle.urls')),
    # path('docs_Route/', include_docs_urls(title = 'Api Route Documentation')),
    # path('docs_ChargePoint/', include_docs_urls(title = 'Api Charge Point Documentation')),
    # path('docs_ElectricVehicle/', include_docs_urls(title = 'Api Electric Vehicle Documentation')),

    # Auth
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/',Toke RefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/',TokenVerifyView.as_view(), name='token_verify'),
]
