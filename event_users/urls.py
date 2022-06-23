from django.urls import path
from . import views

urlpatterns = [
    path('<int:location_id>/', views.EventUserDetailView.as_view(), name='location_detail'),
]