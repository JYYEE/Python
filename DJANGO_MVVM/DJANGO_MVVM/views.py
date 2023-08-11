from django.http import request
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from flask import json
from DJANGO_MVVM.dao_emp import DaoEmp
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def ajax(request):
    #menu = request.GET.get('menu','');
    param =json.loads(request.body)
    print('param', param['menu'])
    context = {
        'result' : 'ok'
        #'menu' : menu
    }
    return JsonResponse(context) 

@csrf_exempt
def ajax_emp_list(request):
    dao = DaoEmp()
    list = dao.selectList()
    context = {
        'list' : list
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_detail(request):
    param = json.loads(request.body)
    e_id = param['e_id']
    #e_id = json.loads(request.body)
    #e_id = request.POST['e_id']
    dao = DaoEmp()
    vo = dao.selectOne(e_id)
    context = {
        'vo' : vo
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_update(request):
    param = json.loads(request.body)
    e_id = param['e_id']
    e_name = param['e_name']
    sex = param['sex']
    addr = param['addr']
    dao = DaoEmp()
    cnt = dao.update(e_id, e_name, sex, addr)
    context = {
        'cnt' : cnt
    }
    return JsonResponse(context)
    
@csrf_exempt
def ajax_emp_add(request):
    param = json.loads(request.body)
    e_id = param['e_id']
    e_name = param['e_name']
    sex = param['sex']
    addr = param['addr']
    dao = DaoEmp()
    cnt = dao.insert(e_id, e_name, sex, addr)
    context = {
        'cnt' : cnt
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_del(request):
    param = json.loads(request.body)
    e_id = param['e_id']
    dao = DaoEmp()
    cnt = dao.delete(e_id)
    context = {
        'cnt' : cnt
    }
    return JsonResponse(context)


