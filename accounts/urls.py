"""
Account url api
"""
from django.urls import path
from rest_auth.views import LoginView

from .views import HomeTemplateView, LogoutViewEx, TestAuthView

urlpatterns = [
    path(
        "test_auth/",
        TestAuthView.as_view(),
        name="test_auth",
    ),
    path(
        "rest-auth/logout/",
        LogoutViewEx.as_view(),
        name="rest_logout",
    ),
    path(
        "rest-auth/login/",
        LoginView.as_view(),
        name="rest_login",
    ),
    path(
        "",
        HomeTemplateView.as_view(),
        name="home",
    ),
]
