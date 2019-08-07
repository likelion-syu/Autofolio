from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
   path('create', views.draft, name='draft')
]
=======
from django.urls import path , include
from . import views

urlpatterns = [
    path('list' , views.draft_list , name="draft_list"),
	path('detail' , views.draft_detail , name="draft_detail"),
]
>>>>>>> d360ac2e76473f663c2c05c35b60b8a78cd14e17
