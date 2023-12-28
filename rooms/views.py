from math import ceil
from django.utils import timezone
from django.views.generic import ListView, DetailView, View
from django.urls import reverse
from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse
from django_countries import countries
from . import models, forms

class HomeView(ListView):
    """Homeview Defintion"""
    model = models.Room
    paginate_by = 10
    ordering = "created"
    pagination_orphans = 5
    page_kwarg = "page"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context
    
class RoomDetail(DetailView):
    model = models.Room
    pk_url_kwarg = 'pk'

class SearchView(View):
    def get(self, request):
        country = request.GET.get("country")
        
        if country:
            form = forms.SearchForm(request.GET)
            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args['room_type'] = room_type

                if price is not None:
                    filter_args['price__lte'] = price

                if guests is not None:
                    filter_args['guests__gte'] = guests

                if bedrooms is not None:
                    filter_args['bedrooms__gte'] = bedrooms

                if beds is not None:
                    filter_args['beds__gte'] = beds

                if baths is not None:
                    filter_args['baths__gte'] = baths

                if instant_book:
                    filter_args['instant_book'] = True
                
                if superhost:
                    filter_args['host__superhost'] = True

                for amenity in amenities:
                    filter_args['amenities'] = amenity
                    
                for facility in facilities:
                    filter_args['facilities'] = facility

                rooms = models.Room.objects.filter(**filter_args)
                return render(request, "rooms/search.html", {
                    "form": form,
                    "rooms": rooms
                })

        else:
            form = forms.SearchForm()

        return render(request, "rooms/search.html", {
            "form": form,
        })


def search(request):
    country = request.GET.get("country")

    if country:
        form = forms.SearchForm(request.GET)
        if form.is_valid():
            city = form.cleaned_data.get("city")
            country = form.cleaned_data.get("country")
            room_type = form.cleaned_data.get("room_type")
            price = form.cleaned_data.get("price")
            guests = form.cleaned_data.get("guests")
            bedrooms = form.cleaned_data.get("bedrooms")
            beds = form.cleaned_data.get("beds")
            baths = form.cleaned_data.get("baths")
            instant_book = form.cleaned_data.get("instant_book")
            superhost = form.cleaned_data.get("superhost")
            amenities = form.cleaned_data.get("amenities")
            facilities = form.cleaned_data.get("facilities")

            filter_args = {}

            if city != "Anywhere":
                filter_args["city__startswith"] = city

            filter_args["country"] = country

            if room_type is not None:
                filter_args['room_type'] = room_type

            if price is not None:
                filter_args['price__lte'] = price

            if guests is not None:
                filter_args['guests__gte'] = guests

            if bedrooms is not None:
                filter_args['bedrooms__gte'] = bedrooms

            if beds is not None:
                filter_args['beds__gte'] = beds

            if baths is not None:
                filter_args['baths__gte'] = baths

            if instant_book:
                filter_args['instant_book'] = True
            
            if superhost:
                filter_args['host__superhost'] = True

            for amenity in amenities:
                filter_args['amenities'] = amenity
                
            for facility in facilities:
                filter_args['facilities'] = facility

            rooms = models.Room.objects.filter(**filter_args)
            return render(request, "rooms/search.html", {
                "form": form,
                "rooms": rooms
            })

    else:
        form = forms.SearchForm()

    return render(request, "rooms/search.html", {
        "form": form,
    })

def search_old_working(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country","NI")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("superhost", False))
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")
    
    form = {
        "city": city,
        "s_room_type":room_type,
        "s_country":country,
        "price":price,
        "guests":guests,
        "bedrooms":bedrooms,
        "beds":beds,
        "baths":baths,
        "s_amenities":s_amenities,
        "s_facilities":s_facilities,
        "instant":instant,
        "superhost":superhost
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities
    }

    # qs = models.Room.objects.filter()
    # if price != 0:
    #     qs = qs.filter(price__lte=price)
    
    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country"] = country

    if room_type != 0:
        filter_args['room_type__pk__exact'] = room_type

    if price != 0:
        filter_args['price__lte'] = price

    if guests != 0:
        filter_args['guests__gte'] = guests

    if bedrooms != 0:
        filter_args['bedrooms__gte'] = bedrooms

    if beds != 0:
        filter_args['beds__gte'] = beds

    if baths != 0:
        filter_args['baths__gte'] = baths

    if instant:
        filter_args['instant_book'] = True
    
    if superhost:
        filter_args['host__superhost'] = True

    if len(s_amenities):
        s_amenities = [int(i) for i in s_amenities]
        filter_args['amenities__in'] = s_amenities
        # for s_amenity in s_amenities:
        #     filter_args['amenities__pk'] = int(s_amenity)

    if len(s_facilities):
        s_facilities = [int(i) for i in s_facilities]
        filter_args['facilities__in'] = s_facilities

    rooms = models.Room.objects.filter(**filter_args).distinct()
    # print(rooms.query)

    return render(request, "rooms/search_old_working.html", {
        **form,
        **choices,
        "rooms": rooms
    })
    
def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room":room})
    except models.Room.DoesNotExist:
        # return redirect(reverse("core:home"))
        raise Http404()

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