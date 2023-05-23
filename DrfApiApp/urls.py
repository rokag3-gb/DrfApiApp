"""
URL configuration for DrfApiApp project.

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
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
#from django.urls import include, path
from rest_framework import routers
#from DrfApiApp.myapp import views
from myapp.views import ClassListAPI, ClassDetail
from myapp.views import UserCreditListAPI, UserCreditDetail
from myapp.views import BookListAPI, BookDetail
from myapp.views import UserBookListAPI

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)

api_ver='api/v1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(api_ver + '/class/', ClassListAPI.as_view()),
    path(api_ver + '/class/<int:pk>/', ClassDetail.as_view()),
    path(api_ver + '/usercredit/', UserCreditListAPI.as_view()),
    path(api_ver + '/usercredit/<int:pk>/', UserCreditDetail.as_view()),
    path(api_ver + '/book/', BookListAPI.as_view()),
    path(api_ver + '/book/<int:pk>/', BookDetail.as_view()),
    path(api_ver + '/userbook/', UserBookListAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)