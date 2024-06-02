from django.urls import path
from .views import UserSignupView, UserLoginView, DashBoard

urlpatterns = [
    path("auth/signup/", UserSignupView.as_view(), name="auth-signup"),
    path("auth/login/", UserLoginView.as_view(), name="auth-login"),
    path("dashboard/", DashBoard.as_view(), name="user-dashboard"),
]
