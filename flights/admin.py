from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class AiportAdmin(admin.ModelAdmin):
    list_display = ("id", "city", "code")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport, AiportAdmin)
admin.site.register(Passenger, PassengerAdmin)