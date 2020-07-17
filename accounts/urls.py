from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignUpView

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    # path('login/', auth_views.LoginView.as_view(template_name='auth/register.html'), name='login'),
    # path('change-password', auth_views.PasswordChangeView.as_view(), name='change-password'),
    # path('logout', auth_views.LogoutView.as_view(), name='logout')
]