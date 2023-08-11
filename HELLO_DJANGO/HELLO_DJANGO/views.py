from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from HELLO_DJANGO.dao_emp import DaoEmp
from HELLO_DJANGO import dao_emp
def hello_django(request):
    return HttpResponse("<h2>Hello, Django!</h2>")

# HttpResponse : 내용을 보내주는 방법

def param(request):
    menu = request.GET.get('menu', 'none') # get 방식 파라미터 받기
    return HttpResponse(f"<h2>get : {menu}</h2>")

@csrf_exempt # post방식 에러나는거 풀어주는 방법. 함수 바로 위에다가 작성. 또는 settings46번째줄 주석처리 
def post(request):
    menu = request.POST['menu'] # post 방식 파라미터 받기
    return HttpResponse(f"<h2>post :{menu}</h2>")

def forw(request):
    a = "홍길동"
    b =["손흥민", "이강인", "김민재"]
    c =[ # db에서 받아오는 형식
        {'e_id' : '1', 'e_name' : '1', 'sex' : '1', 'addr' : '1'},
        {'e_id' : '2', 'e_name' : '2', 'sex' : '2', 'addr' : '2'},
        {'e_id' : '3', 'e_name' : '3', 'sex' : '3', 'addr' : '3'}
        ]
    return render(request, 'forw.html', {'a' : a, 'b' : b, 'c' : c})


def emp(request):
    dao = DaoEmp()
    list = dao.selectList()
    return render(request, 'emp.html', {'list': list})