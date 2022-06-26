from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('runner-level', views.RunnerLevelViewSet)

urlpatterns = [
    path('', views.UserListView.as_view(), name='users'),
    path('profiles/', include(router.urls)),
    path('<int:user_id>/', views.UserDetailView.as_view(), name='user_detail'),
    # path('profiles/', views.ProfileCreateListView.as_view(), name='profiles'),
    path('profiles/<int:user_id>', views.ProfileCreateListView.as_view(), name='user_specific_profile'),
]