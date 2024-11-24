from django.urls import path
from .views import sign_up, UserLoginView, user_logout, profile, edit_profile

urlpatterns = [
    path("sign_up", sign_up, name="register_page"),
    path("login", UserLoginView.as_view(), name="login_page"),
    path("logout", user_logout, name="logout_page"),
    path("profile", profile, name="profile_page"),
    path("profile/edit", edit_profile, name="update_profile_page"),
]
