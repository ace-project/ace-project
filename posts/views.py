from django.shortcuts import render
from .models import Post

# Create your views here.


# 상백

def index(request):

    posts = Post.objects.all()    # Post 모델 데이터 전부를 조회해서 posts 변수에 저장

    context = {
        'posts': posts,
    }
    
    return render(request, 'posts/posts.html', context)


# 용호




# 영수




# 하은