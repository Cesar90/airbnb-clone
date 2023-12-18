from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def all_rooms(request):
    # print(vars(request))
    # print(dir(request))
    # pass
    # return HttpResponse(content=f"<h1>{now}</h1>")
    now = datetime.now()
    hungry = True
    # print(dir(request.GET.keys()))
    # print(request.GET.keys())
    # print(request.GET.get("page", 1))
    page = int(request.GET.get("page", 1))
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    return render(request, "rooms/home.html", context={
        "now":now,
        "hungry": hungry,
        "rooms": all_rooms
    })