from django.shortcuts import render
from .models import Used
from .tasks import repeat_cheak_info

# Create your views here.

def home(request):
    return render(request,'task/home.html')

def chartline(request):
    repeat_cheak_info.delay()
    ret = Used.objects.all()
    print(ret)
    return render(request,'task/chartline.html',context={'ret':ret})