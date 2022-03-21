from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # django에 내장된 User 모델
from django.contrib import auth  # django에 내장된 auth 모델
from .models import Profile


# Create your views here.


# 상백

# 회원가입 기능
def sign_up(request):
    context = {}

    if request.method == 'POST':
        if (request.POST.get('username') and  # 회원가입 시 받은 아이디와 비밀번호 그리고 이메일이 모두 있는지 확인
            request.POST.get('password') and  
            request.POST.get('email') and
            request.POST.get('password') == request.POST.get('password_check')):
            # 그리고 받은 비밀번호와 비밀번호 확인 내용이 일치하는지 확인

            new_user = User.objects.create_user(    # User 모델에 새로운 유저 생성 / 입력된 아이디와 비밀번호로 생성
                username = request.POST.get('username'),
                password = request.POST.get('password'),
            )

            auth.login(request, new_user)   # 위에서 생성한 유저를 로그인시키기

            user = request.user                  # 로그인된 유저를 user 변수에 저장 / 밑에 코드들도 회원가입 시 받은 데이터를 각 변수에 저장
            email = request.POST.get('email')
            # age = request.POST.get('age')
            # gender = request.POST.get('gender')
            # image = request.FILES.get('image')
            profile = Profile(user=user, email=email, mbti='none', type='none', age=0, gender='none', introduce='none', image='none')
            profile.save()                       # 각 변수를 Profile 모델 필드에 저장하고 save()

            return redirect('index')

        else:
            context['error'] = '아이디, 비밀번호 그리고 이메일을 다시 입력해주세요!'    


    return render(request, 'accounts/sign_up.html', context)




# 로그인 기능
def login(request):
    context = {}

    if request.method == 'POST':   # POST방식으로 요청되었을 때, username과 password가 모두 입력되었다면 등록된 유저인지 검증진행
        if request.POST.get('username') and request.POST.get('password'):
            user = auth.authenticate(
                request,
                username = request.POST.get('username'),
                password = request.POST.get('password'),
            )

            if user is not None:   # 만약 검증이 되었다면, 로그인 시키기
                auth.login(request, user)
                return redirect('index')
            else:
                context['error'] = '아이디와 비밀번호를 다시 입력해주세요!'  # 검증이 되지 않았다면, error 메세지 보내기
        else:
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요!'      # username과 password가 모두 입력되지 않았다면 error 메세지 보내기        

    return render(request, 'accounts/login.html', context)



# 마이페이지
def mypage(request):

    profile = request.user.profile   # 로그인된 유저의 Profile 모델에 접근

    wishlists = request.user.liked_travels.all()  # 로그인된 유저가 좋아요를 누른 포토스팟 목록

    context = {
        'profile': profile,
        'wishlists': wishlists,
    }

    return render(request, 'accounts/mypage.html', context)


# 로그아웃 기능
def logout(request):
    if request.method == 'POST':
        auth.logout(request)

    return redirect('index')





# 용호




# 영수




# 하은