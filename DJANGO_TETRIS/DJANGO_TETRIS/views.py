from django.http import request
from django.shortcuts import render
def tetris(request):
    return render(request, 'tetris.html')