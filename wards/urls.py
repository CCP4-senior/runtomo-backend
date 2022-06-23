from django.urls import path
from . import views

urlpatterns = [
    path('', views.WardListView.as_view(), name='Wards'),
    path('<int:ward_id>/', views.WardDetailView.as_view(), name='specific_ward'),
]