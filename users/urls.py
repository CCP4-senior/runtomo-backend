from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='users'),
    path('<int:user_id>/', views.UserDetailView.as_view(), name='user_detail'),
    # path('runner-types/', views.RunnerTypeListView.as_view(), name='runner_types'),
    path('profiles/', views.ProfileCreateListView.as_view(), name='profiles'),
    path('profiles/<int:user_id>', views.ProfileCreateListView.as_view(), name='user_specific_profile'),
]