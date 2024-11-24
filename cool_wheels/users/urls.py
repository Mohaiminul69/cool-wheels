from django.urls import path
from .views import sign_up, UserLoginView, user_logout

urlpatterns = [
    path("sign_up", sign_up, name="register_page"),
    path("login", UserLoginView.as_view(), name="login_page"),
    path("logout", user_logout, name="logout_page"),
]
