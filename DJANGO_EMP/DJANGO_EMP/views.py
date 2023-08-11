from django.http import request
from DJANGO_EMP.dao_emp import DaoEmp
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
def emp_list(request):
    dao = DaoEmp()
    list = dao.selectList()
    return render(request, 'emp_list.html', {'list' : list})

def emp_detail(request):
    e_id = request.GET.get('e_id', '')
    dao = DaoEmp()
    vo = dao.selectOne(e_id)
    return render(request, 'emp_detail.html', {'vo' : vo})


def emp_mod(request):
    e_id = request.GET.get('e_id', '')
    dao = DaoEmp()
    vo = dao.selectOne(e_id)
    return render(request, 'emp_mod.html', {'vo': vo})

@csrf_exempt 
def emp_mod_act(request):
    e_id = request.POST['e_id']
    e_name = request.POST['e_name']
    sex = request.POST['sex']
    addr = request.POST['addr']
    dao = DaoEmp()
    cnt = dao.update(e_id, e_name, sex, addr)
    return render(request, 'emp_mod_act.html', {'cnt' : cnt})

def emp_add(request):
    return render(request, 'emp_add.html')

@csrf_exempt
def emp_add_act(request):
    e_id = request.POST['e_id']
    e_name = request.POST['e_name']
    sex = request.POST['sex']
    addr = request.POST['addr']
    dao = DaoEmp()
    cnt = dao.insert(e_id, e_name, sex, addr)
    return render(request, 'emp_add_act.html', {'cnt' : cnt} )

@csrf_exempt
def emp_del_act(request):
    e_id = request.POST['e_id']
    dao = DaoEmp()
    cnt = dao.delete(e_id)
    return render(request, 'emp_del_act.html', {'cnt' : cnt})
    