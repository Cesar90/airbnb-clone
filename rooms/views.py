from math import ceil
from datetime import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse
from . import models

# Create your views here.
def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", context={
            "page": rooms
        })
    except EmptyPage:
        # rooms = paginator.page(1)
        # rooms = paginator.get_page(page)
        return redirect("/")
    
    

def all_rooms_old(request):
    # print(vars(request))
    # print(dir(request))
    # pass
    # return HttpResponse(content=f"<h1>{now}</h1>")
    now = datetime.now()
    hungry = True
    # print(dir(request.GET.keys()))
    # print(request.GET.keys())
    # print(request.GET.get("page", 1))
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)
    return render(request, "rooms/home_old.html", context={
        "now":now,
        "hungry": hungry,
        "rooms": all_rooms,
        "page": page,
        "page_count": ceil(page_count),
        "page_range": range(1, page_count)
    })