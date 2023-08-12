from django.urls import path
from .views import signup



urlpatterns = [
    path('account/singup/', signup, name='signup'),
    path('account/singup/', signup, name='login'),
]