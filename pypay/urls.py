from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('geeky.urls', namespace='geeky')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/cashy/', include('daraja.api.urls')),
]
