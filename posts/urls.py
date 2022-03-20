from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    # Navbar 함께하기 버튼 클릭 시 URL
    path('', views.index, name='index'),

    # 게시판 디테일 페이지 URL
    path('<int:post_id>/', views.detail, name='detail'),

    # 게시판 디테일 페이지 댓글 생성
    path('<int:post_id>/comment/', views.comment, name='comment'),
]