from django.http import request
from DJANGO_MEM.dao_mem import DaoMem
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
def mem_list(request):
    dao = DaoMem()
    list = dao.selectList()
    return render(request, 'mem_list.html', {'list' : list})

def mem_detail(request):
    m_id = request.GET.get('m_id', '')
    dao = DaoMem()
    vo = dao.selectOne(m_id)
    return render(request, 'mem_detail.html', {'vo' : vo})


def mem_mod(request):
    m_id = request.GET.get('m_id', '')
    dao = DaoMem()
    vo = dao.selectOne(m_id)
    return render(request, 'mem_mod.html', {'vo': vo})

@csrf_exempt 
def mem_mod_act(request):
    m_id = request.POST['m_id']
    m_name = request.POST['m_name']
    tel = request.POST['tel']
    address = request.POST['address']
    dao = DaoMem()
    cnt = dao.update(m_id, m_name, tel, address)
    return render(request, 'mem_mod_act.html', {'cnt' : cnt})

def mem_add(request):
    return render(request, 'mem_add.html')

@csrf_exempt
def mem_add_act(request):
    m_id = request.POST['m_id']
    m_name = request.POST['m_name']
    tel = request.POST['tel']
    address = request.POST['address']
    dao = DaoMem()
    cnt = dao.insert(m_id, m_name, tel, address)
    return render(request, 'mem_add_act.html', {'cnt' : cnt} )

@csrf_exempt
def mem_del_act(request):
    m_id = request.POST['m_id']
    dao = DaoMem()
    cnt = dao.delete(m_id)
    return render(request, 'mem_del_act.html', {'cnt' : cnt})
    

