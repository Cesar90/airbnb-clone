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
    all_rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={
        "now":now,
        "hungry": hungry,
        "rooms": all_rooms
    })