
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("profile/<str:username>/addpost", views.addpost, name="addpost"),
    path("followings/<str:username>", views.follow, name='follow'),
    path("posts/<int:post_id>/edit", views.edit, name="edit"),
    url(r'search/$', views.search, name="search"),
    url(r'^likings/$', views.likings, name='likings')
]
