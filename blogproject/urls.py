"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name="home"),
    path('blog/<str:id>',blog.views.detail, name="detail"),
    path('blog/',blog.views.index, name="index"),
    path('about_me/',blog.views.about_me, name="about_me"),
    path('delete/<str:id>',blog.views.delete, name="delete"),
    path('create/',blog.views.create,name="create"),
    path('edit/<str:id>',blog.views.edit,name="edit"),
    path('update/<str:id>',blog.views.update,name="update"),
    path('new/',blog.views.new, name="new"),
]
