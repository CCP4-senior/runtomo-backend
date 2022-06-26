from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

class OptionalSlashRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):        
        super(DefaultRouter, self).__init__(*args, **kwargs)        
        self.trailing_slash = '/?' 

router = OptionalSlashRouter()
router.register('profile', views.ProfileViewSet)
router.register('runner-level', views.RunnerLevelViewSet)

urlpatterns = [
    path('', views.UserListView.as_view(), name='users'),
    path('<int:user_id>/', views.UserDetailView.as_view(), name='user_detail'),
    path('', include(router.urls)),
]