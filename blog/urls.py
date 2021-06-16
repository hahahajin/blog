from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('<str:id>', views.detail, name="detail"),
    path('index/',views.index, name="index"),
    path('about_me/',views.about_me, name="about_me"),
    path('delete/<str:id>',views.delete, name="delete"),
    path('create/',views.create,name="create"),
    path('edit/<str:id>',views.edit,name="edit"),
    path('update/<str:id>',views.update,name="update"),
    path('new/',views.new, name="new"),
    
]

