from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    ##CREATE
    path('new/', views.draft_new, name='draft_new'),
    path('crete/', views.draft_create, name='draft_create'),
    ##READ
    path('', views.draft_list, name="draft_list"),
	path('detail/', views.draft_detail , name="draft_detail"),  # 오류파티
    ##UPDATE
    path('edit/<int:draft_id>/', views.draft_edit, name='draft_edit'),
    path('update/<int:draft_id>/', views.draft_update, name='draft_update'),
    ##DELETE
    path('delete/<int:draft_id>/', views.draft_delete, name='draft_delete'),
]
