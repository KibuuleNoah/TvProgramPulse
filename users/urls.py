from django.urls import path
from .views import UserSignupView, UserLoginView, DashBoard, LogOutUser

urlpatterns = [
    path("auth/signup/", UserSignupView.as_view(), name="auth-signup"),
    path("auth/login/", UserLoginView.as_view(), name="auth-login"),
    path("auth/logout/", LogOutUser.as_view(), name="auth-logout"),
    path("dashboard/", DashBoard.as_view(), name="user-dashboard"),
]
