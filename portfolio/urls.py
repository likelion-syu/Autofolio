from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
	path('list' , views.portfolio_list , name="portfolio_list"),
	path('detail' , views.portfolio_detail , name="portfolio_detail"),
	path('preview' , views.portfolio_preview , name="portfolio_preview"),
	path('create' , views.portfolio_create , name="portfolio_create"),
	path('update' , views.portfolio_update , name="portfolio_update"),
]