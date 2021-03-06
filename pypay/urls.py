from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="GeekforHumans API",
      default_version='v1',
      description="GeekforHumans API is a good place to be!",
      terms_of_service="https://www.geekforhumans.com/policies/terms/",
      contact=openapi.Contact(email="master@noriahub.com"),
      license=openapi.License(name="GeekforHumans License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('geeky.urls', namespace='geeky')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/cashy/', include('daraja.api.urls')),

    path('swagger(?<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
