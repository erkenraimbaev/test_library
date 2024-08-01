from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from readers.apps import UsersConfig
from readers.views import RegisterView, ProfileView, confirm_email

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='readers/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]