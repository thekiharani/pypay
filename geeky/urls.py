from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('notes', views.NoteView)

urlpatterns = [
    path('', include(router.urls)),
]

app_name = 'geeky'