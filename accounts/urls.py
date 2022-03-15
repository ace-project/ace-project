from unicodedata import name
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # 회원가입 URL 설정
    path('sign_up/', views.sign_up, name='sign_up'),

    # 로그인 URL 설정
    path('login/', views.login, name='login'),

    # 마이페이지 URL 설정
    path('mypage/', views.mypage, name='mypage'),

    # 로그아웃 URL 설정
    path('logout/', views.logout, name='logout'),
]