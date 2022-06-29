from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.HelloAuthView.as_view(), name = 'youre_in_auth'),
    path('signup/', views.UserCreateView.as_view(), name='sign_up'),
    path('update/', views.UserUpdateView.as_view(), name='update_user'),
    path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='auth_change_password'),

]