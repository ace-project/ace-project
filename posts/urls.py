from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    # Navbar 함께하기 버튼 클릭 시 URL
    path('', views.index, name='index'),
]