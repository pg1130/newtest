"""
URL configuration for mysite project.

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
from django.urls import include, path

from mysite.views import HomeView # 추가

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    #path('', include('myapi.urls')), #api/urls.py 를 사용
    path('', HomeView.as_view(),name="home"), #INDEX 페이지 신규구성(2023-08-01)
    path("bookmark/", include("bookmark.urls")), # bookmark app 경로 추가
    path("blog/",include('blog.urls'),name='blog'), #blog app 경로 추가
    path("person/",include('person.urls'),name='person'), #blog app 경로 추가
]