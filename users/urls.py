from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='users'),
    path('<int:id>/', views.UserDetailView.as_view(), name='user_detail'),
    # path('runner-types/', views.RunnerTypeListView.as_view(), name='runner_types'),
    path('profiles/', views.ProfileCreateListView.as_view(), name='profiles'),
    # path('profiles/<int:id>', views.ProfileCreateListView.as_view(), name='profile_create'),
    # path('<int:event_id>/', views.EventDetailView.as_view(), name='event_detail'),
    # path('user/<int:user_id>/events/', views.UserEventsView.as_view(), name='users_events'),
    # path('user/<int:user_id>/events/<int:event_id>/', views.UserEventDetails.as_view(), name='user_specific_event'),
]