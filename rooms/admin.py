from django.contrib import admin
from . import models

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
        """
                Item Admin Definition
        """
        pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
        """
                Room Admin Definition
        """

        fieldsets = (
        (
                "Basic Info",
                {
                        "fields": (
                                "name",
                                "description",
                                "country",
                                "city",
                                "address",
                                "price",
                                "room_type",
                        )
                },
                ),
                ("Times", {"fields": (
                                "check_in", 
                                "check_out", 
                                "instant_book"
                                )}),
                ("Spaces", 
                        {"fields": (
                                "guests",
                                "beds",
                                "bedrooms",
                                "baths"
                        )}),
                (
                "More About the Space",
                        {"fields": 
                                (
                                        "amenities",
                                        "facilities",
                                        "house_rules"
                                )},
                ),
                ("Last Details", {"fields": ("host",)}),
        )

        list_display = (
                "name",
                # "description",
                "country",
                "city",
                "price",
                "guests",
                "beds",
                "bedrooms",
                "baths",
                "check_in",
                "check_out",
                "instant_book",
                "count_amenities"
        )

        # ordering = (
        #         "name",
        #         "price",
        #         "bedrooms"
        # )

        list_filter = (
                "instant_book",
                "host__superhost",
                "room_type",
                "amenities",
                "facilities",
                "house_rules",
                "city",
                "country",
        )

        search_fields = ("=city","^host__username")

        filter_horizontal = ("amenities", "facilities", "house_rules")

        def count_amenities(self, obj):
                return obj.amenities.count()
        
        count_amenities.short_description = "Count Amenities"

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
        """

        """
        pass