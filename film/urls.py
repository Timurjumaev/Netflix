"""film URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from filmapp.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# router=DefaultRouter()
# router.register("kinolar", KinoViewSet)
# router.register("aktyorlar", AktyorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_token/', TokenObtainPairView.as_view()),
    path('refresh_token/', TokenRefreshView.as_view()),
    path('comments/', CommentsAPIView.as_view()),
    # path('kinolar/', KinolarAPIView.as_view()),
    # path('aktyorlar/', AktyorlarAPIView.as_view()),
    # path('aktyor/<int:son>/', AktyorAPIView.as_view()),

    # path('', include(router.urls))
]
