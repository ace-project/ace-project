"""ace URL Configuration

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
from django.urls import path, include
from django.conf import settings    # 이미지 파일 업로드를 위한 settings import
from django.conf.urls.static import static  # 이미지 파일 업로드를 위한 static import
from travels import views


urlpatterns = [
    # admin 페이지 URL
    path('admin/', admin.site.urls),

    # 메인 index 페이지 URL -> travels 앱의 index View로 연결
    path('', views.index, name="index"),

    # travels로 시작하는 경우, travels 앱의 urls.py로 연결
    path('travels/', include('travels.urls')),

    # posts로 시작하는 경우, posts 앱의 urls.py로 연결
    path('posts/', include('posts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  # 이미지 serving를 위해 settings에서 설정한 MEDIA_URL로 요청이 들어올 경우, MEDIA_ROOT 내부에서 검색 후 HTTP Response로 응답
