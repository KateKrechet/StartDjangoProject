"""
URL configuration for djangoProject_lesson21 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import re_path
from hello import views

urlpatterns = [
    # форма логин пароль
    path('admin/', admin.site.urls),
    # когда ничего не написано
    path('', views.index),
    # надпись внутри ссылки
    # path('about/', views.about),
    path('home/', views.home, name='home'),
    path('home/month/', views.month),
    path('home/contacts/', views.contacts),
    path('home/workers/', views.workers),
    path('month/<str:id>', views.month, name='url1'),
    path('product/<str:id>', views.product, name='url2'),
    path('spisok/', views.spisok, name='spisok'),
    # path('proverka/<int:year>', views.proverka),
    re_path(r'proverka/(?P<year>\d{4})', views.proverka),
    re_path(r'^about/',views.about)
]
