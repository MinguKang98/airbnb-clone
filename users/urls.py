from django.urls import path
from django.views.generic.edit import FormView
from . import views
from rooms import views as room_views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("login/github", views.github_login, name="github-login"),
    path("login/github/callback", views.github_callback, name="github-callback"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("verify/<str:key>", views.complete_verification, name="complete-verification"),
    path("switch-hosting/", room_views.room_detail, name="switch-hosting"),
    path("update-profile/", views.UpdateUserView.as_view(), name="update"),
    path("update-password/", views.UpdatePasswordView.as_view(), name="password"),
    path("<int:pk>/", views.UserPofileView.as_view(), name="profile"),
]
