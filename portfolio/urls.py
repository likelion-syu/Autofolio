from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
	path('' , views.portfolio_list , name="portfolio_list"),
	path('preview' , views.portfolio_preview , name="portfolio_preview"),
	path('create' , views.portfolio_create , name="portfolio_create"),
	path('update/<int:portfolio_id>' , views.portfolio_update , name="portfolio_update"),
	path('api/create' , views.api_create , name="portfolio_api_create"),
	path('api/delete' , views.api_delete , name="portfolio_api_delete"),
	path('api/update' , views.api_update , name="portfolio_api_update"),
]