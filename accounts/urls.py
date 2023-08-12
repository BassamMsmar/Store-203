from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, activate_email



urlpatterns = [
    path('accounts/singup/', signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/activate/<int:uid>/<token>/', activate_email, name='activate_email'),
]