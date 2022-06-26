from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter(trailing_slash=False)
router.register('profile', views.ProfileViewSet)
router.register('runner-level', views.RunnerLevelViewSet)

urlpatterns = [
    path('', views.UserListView.as_view(), name='users'),
    path('<int:user_id>/', views.UserDetailView.as_view(), name='user_detail'),
    path('', include(router.urls)),
    # path('profile/', views.ProfileViewSet.as_view({'post':'create'})),
    # path('profile/<int:user_id>', views.ProfileViewSet.as_view({'patch': 'partial_update'})),
    # path('profiles/', views.ProfileCreateListView.as_view(), name='profiles'),
    # path('profile/<int:user_id>', views.ProfileCreateListView.as_view(), name='user_specific_profile'),
]