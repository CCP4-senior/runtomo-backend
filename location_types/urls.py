from django.urls import path
from . import views

urlpatterns = [
    path('<int:location_type_id>/', views.LocationTypeDetailView.as_view(), name='location_type_detail'),
]