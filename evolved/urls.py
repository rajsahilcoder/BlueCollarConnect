from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path('',views.home,name='home'),
    path("cook/", views.cook, name="cook"),
    path("content_based/", views.content_based, name="content_based"),
    path("collaborative/", views.collaborative, name="collaborative"),
]