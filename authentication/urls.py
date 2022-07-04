from django.urls import path, re_path, include
from . import views

urlpatterns = [
    # path('', views.HelloAuthView.as_view(), name = 'youre_in_auth'),
    re_path('^signup/?$', views.UserCreateView.as_view(), name='sign_up'),
    re_path('^update/?$', views.UserUpdateView.as_view(), name='update_user'),
    re_path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='auth_change_password'),
    re_path('^delete/?$', views.UserDeleteView.as_view(), name='delete_user'),
]