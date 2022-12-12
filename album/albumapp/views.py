
from django.http import HttpResponse
from django.shortcuts import render
from .models import Engagement, Mk_sreya, Mk_sethu, Wedding


def home(request):
    return render(request,"home.html")

def eng(request):
    e = Engagement.objects.all()
    content = {'engagement_list': e}
    return render(request, "engagement.html", content)

def mk_sreya(request):
    mk_sreya = Mk_sreya.objects.all()
    content = {'mk_sreya_list': mk_sreya}
    return render(request, "mk_sreya.html", content)

def mk_sethu(request):
    mk_sethu = Mk_sethu.objects.all()
    content = {'mk_sethu_list': mk_sethu}
    return render(request, "mk_sethu.html", content)

def wedding(request):
    wedding = Wedding.objects.all()
    content = {'wedding_list': wedding}
    return render(request, "wedding.html", content)