from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/create_comment/', views.EventCommentCreate.as_view(), name='event_comment_create'),
    path('<int:pk>/comments/', views.EventCommentList.as_view(), name='event_comment_list'),
    path('comment/<int:pk>/', views.CommentDetail.as_view(), name='event_comment_detail'),
]