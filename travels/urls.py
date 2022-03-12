from django.urls import path, include
from . import views

app_name = 'travels'

urlpatterns = [
    # Navbar 지도 버튼 클릭 시 URL
    path('map/', views.map, name='map'),
]

