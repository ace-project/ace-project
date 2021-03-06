from unicodedata import name
from django.urls import path, include
from . import views

app_name = 'travels'

urlpatterns = [
    # Navbar 지도 버튼 클릭 시 URL
    path('map/', views.map, name='map'),

    # Navbar 둘러보기 버튼 클릭 시 URL
    path('spots/', views.spots, name='spots'),

    # 포토스팟 디테일 페이지 URL
    path('spots/<int:travel_id>/', views.spot, name='spot'),

    # 포토스팟 1개 좋아요 URL
    path('spots/<int:travel_id>/like/', views.spotlike, name='spotlike'),

    # 포토스팟 1개 댓글 생성 URL
    path('spots/<int:travel_id>/comment/', views.comment, name='comment'),

    # 포토스팟 1개 댓글 삭제 URL
    path('spots/<int:travel_id>/comment/<int:comment_id>/', views.comment_delete, name="comment_delete")
]


