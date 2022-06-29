from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventCreateListView.as_view(), name='Events'),
    path('<int:event_id>/', views.EventDetailView.as_view(), name='event_detail'),
    path('user/<int:user_id>/events/', views.UserEventsView.as_view(), name='users_events'),
    path('user/<int:user_id>/events/<int:event_id>/', views.UserEventDetails.as_view(), name='user_specific_event'),
]