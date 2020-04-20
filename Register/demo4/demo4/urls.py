"""demo4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app01.views import SendCodeView,RegisterView
from app01.views import SendActiveCodeView,ActiveView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendcode/', SendCodeView.as_view(),name='sendcode'),
    path('register/',RegisterView.as_view(),name='register'),
    path('sendactivecode/',SendActiveCodeView.as_view(),name='sendactivecode'),
    path('active/<str:code>',ActiveView.as_view(),name='active'),
]
