""" Posts URLs. """

# Django 
from django.urls import path

# Views 
from .views import PostFeedView, PostDetailView, CreatePostView

urlpatterns = [
    path(route='',  view=PostFeedView.as_view(), name='feed'),
    # path(route='posts/new/', view=create_post, name='create'),
    path(route='posts/new/', view=CreatePostView.as_view(), name='create'),
    path(route='posts/<int:pk>/', view=PostDetailView.as_view(), name='detail')
]

    