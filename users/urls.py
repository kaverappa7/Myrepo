from django.urls import path
from . import views
from.views import dashboard_view

urlpatterns = [
    path("signup/",views.signup,name="signup"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("dashboard/",dashboard_view,name="dashboard"),
]