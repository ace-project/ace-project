from django.shortcuts import render
from .models import Travel
from django.db.models import Q  # 모델 filter를 하기 위해 import
import requests # API HTTP Request 전송을 하기 위해 requests 라이브러리 import

# Create your views here.


# 상백



# 메인페이지
def index(request):

    return render(request, 'travels/index.html')




# 카카오맵 API 이용해서 지도 보여주기
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





# 용호





# 영수




# 하은
