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

    # 게시판 디테일 페이지 댓글 삭제
    path('<int:post_id>/comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),

    # 게시판 글 생성하기 
    path('create/', views.create, name='create'),

    # 게시판 글 수정하기
    path('<int:post_id>/edit/', views.edit, name='edit'),

    # 게시판 글 삭제하기
    path('<int:post_id>/delete/', views.delete, name='delete'),
]