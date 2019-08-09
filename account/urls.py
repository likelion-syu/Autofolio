from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.index , name="home"),
    path('signin', views.signin , name="signin"),
    path('signup', views.signup , name="signup"),
    path('logout', views.logout , name="logout"),
    path('find', views.account_find , name="account_find"),
    path('user', views.account_detail , name="account_detail"),
    path('edit/user', views.account_edit , name="account_edit"),
]
