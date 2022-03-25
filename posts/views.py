from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from travels.models import Comment, Travel
from accounts.models import Profile
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.


# 상백

# 게시판 리스트
def index(request):
 
   posts = Post.objects.all().order_by('-id')    # Post 모델 데이터 전부를 조회해서 posts 변수에 저장
   

   # 페이지네이터 코드
   paginator = Paginator(posts, 5)
   page = request.GET.get('page')
   posts = paginator.get_page(page)

   page_range = paginator.page_range



   # 검색 기능
   q = request.GET.get('query', '')
   if q:
       posts = Post.objects.all().filter(title__icontains=q)


   
   context = {
       'posts': posts,
       'page_range': page_range,
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
@login_required
def comment(request, post_id):
    
   if request.method == 'POST':
        user = request.user
        author = Profile.objects.get(user=user)
    
        content = request.POST.get('content')
        post = Post.objects.get(id=post_id)
        
        secret = request.POST.get('secret_comment', 'False')
    
        comment = Comment(author=author, content=content, created_at=timezone.now(), post=post, secret=secret)
        comment.save()

        return redirect('posts:detail', post_id=post.id)
   return redirect('posts:detail', post_id=post.id)  
    


 
                


# 게시판 디테일 페이지 댓글 삭제
def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = Post.objects.get(pk=post_id)

    comment.delete()

    return redirect('posts:detail', post_id=post.id)



# 게시판 글 생성하기
@login_required
def create(request):
    travels = Travel.objects.all()

    if request.method == 'POST':
        user = request.user
        user = Profile.objects.get(user=user)
        title = request.POST.get('title')
        body = request.POST.get('body')
        # due = request.POST.get('due')
        # location = request.POST.get('photospot')

        post = Post(user=user, title=title, body=body, location='none')
        post.save()

        return redirect('posts:index')

    context = {
        'travels': travels,
    }

    return render(request, 'posts/create.html', context)


# 게시판 글 수정하기
@login_required
def edit(request, post_id):

    try:
        post = Post.objects.get(id=post_id, user=request.user.profile)   # 본인일 경우에만 수정할 수 있도록 설정
        travels = Travel.objects.all()
    except Post.DoesNotExist:
        return redirect('posts:index')

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.body = request.POST.get('body')
        # post.due = request.POST.get('due')
        # post.location = request.POST.get('photospot')
        post.save()

        return redirect('posts:detail', post_id=post.id)

    context = {
        'post': post,
        'travels': travels,
    }

    return render(request, 'posts/edit.html', context)


# 게시판 글 삭제하기
@login_required
def delete(request, post_id):

    try:
        post = Post.objects.get(id=post_id, user=request.user.profile)
        post.delete()
    except Post.DoesNotExist:
        return redirect('posts:index')     

    return redirect('posts:index')


# 용호




# 영수




# 하은