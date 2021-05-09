from django.contrib import admin
from login.models import Customer, RoomManager
from booking.models import Contact,Room,Booking
# Register your models here.
admin.site.register(Customer)
admin.site.register(RoomManager)
admin.site.register(Contact)
admin.site.register(Room)
admin.site.register(Booking)