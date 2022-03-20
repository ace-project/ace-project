from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Post
from travels.models import Comment
from accounts.models import Profile
from django.utils import timezone

# Create your views here.


# 상백

# 게시판 리스트
def index(request):
 
   posts = Post.objects.all()    # Post 모델 데이터 전부를 조회해서 posts 변수에 저장
   
 
   context = {
       'posts': posts,
   }
  
   return render(request, 'posts/posts.html', context)
 
 
 
# 게시판 디테일 페이지
def detail(request, post_id):
 
   post = Post.objects.get(id=post_id)   # Posts 모델 데이터 1개 조회 후 post 변수에 저장
 
   context = {
       'post': post,
   }
 
   return render(request, 'posts/detail.html', context)
 
 
 
# 게시판 디테일 페이지 댓글
def comment(request, post_id):
   if request.method == 'POST':
       user = request.user
       author = Profile.objects.get(user=user)
 
       content = request.POST.get('content')
       post = Post.objects.get(id=post_id)
 
       comment = Comment(author=author, content=content, created_at=timezone.now(), post=post)
       comment.save()
 
       return redirect('posts:detail', post_id=post.id)


# 용호




# 영수




# 하은