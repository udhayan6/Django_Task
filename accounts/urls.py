from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home),
    path('/login/', LoginView.as_view(template_name="accounts/login.html")),
    path('/logout/', LogoutView.as_view(template_name="accounts/logout.html")),
    path('/register/', views.register)
]
 