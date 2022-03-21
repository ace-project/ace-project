from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Travel, Comment
from django.db.models import Q  # 모델 filter를 하기 위해 import
import requests # API HTTP Request 전송을 하기 위해 requests 라이브러리 import
from django.contrib.auth.decorators import login_required # 로그인된 유저만 접근할 수 있도록 import
from accounts.models import Profile
from django.utils import timezone
import random
from django.db.models import Count

# Create your views here.


# 상백



##### github 수정

# 메인페이지
# 아래에 영수 수정


# 둘러보기 페이지
def spots(request):
    listtype = request.GET.get('listtype', '')  # listtype이라는 이름으로 GET방식으로 보낸 데이터를 저장

    if listtype == '최신순':
        travels = Travel.objects.all().order_by('-id')  # Travel 모델 pk 기준 내림차순으로 데이터 정렬하기(최신순)
    elif listtype == '인기순':
        travels = Travel.objects.annotate(like=Count('liked_users__liked_travels')).order_by('-like', '-id')
        # 좋아요순으로 내림차순 / 좋아요 개수가 같으면 id 내림차순으로 설정  
    else:
        travels = Travel.objects.all()  # Travel 모델 데이터 전부 다 travels라는 변수에 저장


    locationsearch = request.GET.get('locationsearch', '')  # locationsearch라는 이름으로 GET방식으로 보낸 데이터를 저장

    if locationsearch == '제주전체':                          # 데이터 value에 따라 Travel 모델 필드값을 필터링해서 보여주기
        travels = Travel.objects.all().filter(location__icontains='jeju')
    elif locationsearch == '제주시':
        travels = Travel.objects.all().filter(region__icontains='제주시')    
    elif locationsearch == '한림읍':
        travels = Travel.objects.all().filter(region__icontains='한림읍')
    elif locationsearch == '한경면':
        travels = Travel.objects.all().filter(region__icontains='한경면')
    elif locationsearch == '안덕면':
        travels = Travel.objects.all().filter(region__icontains='안덕면')
    elif locationsearch == '성산읍':
        travels = Travel.objects.all().filter(region__icontains='성산읍')
    elif locationsearch == '남원읍':
        travels = Travel.objects.all().filter(region__icontains='남원읍')    
    elif locationsearch == '애월읍':
        travels = Travel.objects.all().filter(region__icontains='애월읍') 
    elif locationsearch == '구좌읍':
        travels = Travel.objects.all().filter(region__icontains='구좌읍')      
                       

    q = request.GET.get('query', '')  # 검색창에서 검색한 값은 query라는 이름으로 정했고 GET방식으로 보낸 데이터를 저장

    if q:
        travels = Travel.objects.all().filter(title__icontains=q)  # 포토스팟 제목에 해당 데이터가 들어있으면 보여주기   



    context = {
        'listtype': listtype,
        'locationsearch': locationsearch,
        'q': q,
        'travels': travels,
    }

    return render(request, 'travels/spots.html', context)



# 포토스팟 좋아요 기능
@login_required
def spotlike(request, travel_id):
    
    if request.method == 'POST':
        try:
            travel = Travel.objects.get(id=travel_id)

            if request.user in travel.liked_users.all():
                travel.liked_users.remove(request.user)
            else:
                travel.liked_users.add(request.user)


            return redirect('travels:spots')
        except Travel.DoesNotExist:
            pass        

    elif request.method == 'GET':
        try:
            travel = Travel.objects.get(id=travel_id)

            if request.user in travel.liked_users.all():
                travel.liked_users.remove(request.user)
            else:
                travel.liked_users.add(request.user)


            return redirect('travels:spot', travel_id=travel.id)
        except Travel.DoesNotExist:
            pass        

        
    redirect('travels:spots')




# 포토스팟 디테일 페이지
def spot(request, travel_id):

    travel = Travel.objects.get(id=travel_id)   # 해당 travel_id 데이터를 조회해서 travel이라는 변수에 저장
    

    # 지도 API 기능
    search = travel.address
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query={}'.format(search)
    result = requests.get(url, headers={"Authorization" : "KakaoAK 537c71004ec6bb642b90b8bdf96180e5"})
    result_dictionary = result.json()
    documents = result_dictionary.get('documents')


    context = {
        'search': search,
        'travel': travel,
        'documents': documents,
    }

    return render(request, 'travels/spot.html', context)


# 포토스팟 디테일 페이지 댓글 생성
def comment(request, travel_id):
    if request.method == 'POST':
        author = request.user
        comment_profile = Profile.objects.get(user=author)

        content = request.POST.get('content')

        travel = Travel.objects.get(id=travel_id)

        if not content:
            return redirect('travels:spot', travel_id=travel.id)
        
        Comment.objects.create(author=comment_profile, content=content, created_at=timezone.now(), travel=travel)

    return redirect('travels:spot', travel_id=travel.id)




# 용호
def map(request):


    # Travel이라는 모델 데이터베이스에 저장된 데이터 가져오기
    spots = Travel.objects.all()

    # 입력된 검색 값으로 API request 하기
    search = request.GET.get('search', '')  # HTTP GET방식으로 요청된 검색창에서 입력한 키워드를 저장
    
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(search)   
    # url이라는 변수를 따로 정의해서 카카오 API URL를 저장 / 이 때 검색할 장소인 query의 값은 위의 search로 대체
    result = requests.get(url, headers={"Authorization" : "KakaoAK 537c71004ec6bb642b90b8bdf96180e5"})
    # 카카오 API로 HTTP Request를 GET방식으로 전송 / 헤더에 REST API 키 전달 / API 전송 결과를 result 변수에 저장
    result_dictionary = result.json()
    # API 전송 결과를 json() 형태로 바꾸고 result_dictionary 변수에 저장
    documents = result_dictionary.get('documents')

    context ={
        'search': search,
        'spots': spots,
        'documents': documents,
    }

    return render(request, 'travels/map.html', context)




# 영수

# 메인페이지 
def index(request):
    spots = list(Travel.objects.all())
    spots = random.sample(spots, 6)
    
    context = {
        'spots': spots,

    }

    return render(request, 'travels/index.html', context)



# 하은
