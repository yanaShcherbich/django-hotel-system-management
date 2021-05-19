from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from booking.models import Booking,Room


class RoomResource(resources.ModelResource):

    class Meta:
        model = Room
        #fields = ('manager', 'room_no', 'room_type', 'price', 'no_of_days_advance', 'start_date', 'room_image', 'room_description')

class RoomAdmin(ImportExportModelAdmin):
    resource_class = RoomResource

admin.site.register(Room, RoomAdmin)
