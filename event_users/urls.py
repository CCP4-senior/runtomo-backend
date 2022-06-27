from django.urls import path
from . import views

urlpatterns = [
    path('<int:event_id>/', views.EventUserDetailView.as_view(), name='event_user_detail'),
    path('eventuser/add_user_attendance', views.EventUserDetailView.as_view(), name='event_user_detail')
]