""" Users URLs."""

# Djago
from django.urls import path
from django.views.generic import TemplateView
# view 
from .views import UpdateProfileView, LogoutView, UserDetailView, SingupView, LoginView
# no importa
from django.views.generic import TemplateView

urlpatterns = [
    # Posts
   

    # Management
    path(
        route='login/',
        view=LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='signup/',
        view=SingupView.as_view(),
        name='signup'
    ),
    path(
        route='me/profile/',
        view=UpdateProfileView.as_view(),
        name='update'
    ),
    path(
        route='<str:username>/',
        view=UserDetailView.as_view(),
        name='detail'
    ),
]