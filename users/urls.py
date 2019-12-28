""" Users URLs."""

# Djago
from django.urls import path
from django.views.generic import TemplateView
# view 
from .views import update_profile, signup, login_view, logout_view, UserDetailView
# no importa
from django.views.generic import TemplateView

urlpatterns = [
    # Posts
   

    # Management
    path(
        route='login/',
        view=login_view,
        name='login'
    ),
    path(
        route='logout/',
        view=logout_view,
        name='logout'
    ),
    path(
        route='signup/',
        view=signup,
        name='signup'
    ),
    path(
        route='me/profile/',
        view=update_profile,
        name='update'
    ),
    path(
        route='<str:username>/',
        view=UserDetailView.as_view(),
        name='detail'
    ),
    # path(
    #     route='<str:username>/',
    #     view=TemplateView.as_view(template_name='users/detail.html'),
    #     name='detail'
    # )
]