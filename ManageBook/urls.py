from django.contrib import admin
from django.urls import path,include
from ManageBook import views

urlpatterns = [
  
    path('', views.home,name="home"),
    path("storebook/",views.storebook,name="storebook"),
    path("showbook/",views.showbook,name="showbook"),
    path("edit/<int:id>",views.edit,name="edit"),
    path("delete/<int:id>",views.deleteBook,name="delete"),
]