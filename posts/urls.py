""" Posts URLs. """

# Django 
from django.urls import path

# Views 
from .views import list_posts, create_post

urlpatterns = [
    path(route='',  view=list_posts, name='feed'),
    path(route='posts/new/', view=create_post, name='create'),
]

    