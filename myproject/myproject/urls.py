"""
URL configuration for myproject project.

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
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
from django.contrib import admin
from django.urls import path, include
from myproject import views
# from polls import views

# myproject - urls.py 는 주소 값을 설정하는 곳
urlpatterns = [
    path("", views.HomeView.as_view(), name="Home"),
    path("admin/", admin.site.urls),

    # path 에 polls 라는 경로를 추가해주는 방법, polls 파일 경로에 urls.py 를 가져다 쓰기 위함
    path('polls/', include('polls.urls.py')),
    path('books/', include('books.urls.py')),
    path('stores/', include('stores.urls.py')),
]
