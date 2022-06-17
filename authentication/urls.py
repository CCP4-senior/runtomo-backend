from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HelloAuthView.as_view(), name = 'youre_in_auth'),
    path('signup/', views.UserCreateView.as_view(), name='sign_up'),
]