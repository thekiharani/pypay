from django.urls import path
from daraja.api.views import ExpressCallback

urlpatterns = [
    path('express_callback/', ExpressCallback.as_view(), name='express_callback'),
]
