from django.urls import path
from . import views

urlpatterns = [
    path('', views.PointOfInterestListView.as_view(), name='PointsOfInterest'),
    path('<int:pointsofinterest_id>/', views.PointOfInterestDetailView.as_view(), name='specific_point_of_interest'),
]