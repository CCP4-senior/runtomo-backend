from django.urls import path
from . import views



urlpatterns = [
    path('create_event', views.EventCreateListView.as_view(), name='create_event'),
    path('', views.EventsDetailViewAll.as_view(), name='Events'),
    path('<int:event_id>/', views.EventDetailView.as_view(), name='event_detail'),
    path('user/<int:user_id>/events/', views.UserEventsView.as_view(), name='users_events'),
    path('user/<int:user_id>/events/<int:event_id>/', views.UserEventDetails.as_view(), name='user_specific_event'),
    path('participant/<int:event_id>/', views.ParticipantDetails.as_view(), name='get_participants'),
    path('participant/<int:event_id>/', views.ParticipantDetails.as_view(), name='add_participant')
]