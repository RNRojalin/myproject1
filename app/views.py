from django.shortcuts import render
from django.http import HttpResponse
from django.http import *

def rojalin(request):
    return HttpResponse('Hiiiii')
def xyz(request):
    return render(request,'index.html')