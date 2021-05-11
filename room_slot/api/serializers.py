from rest_framework import serializers
from login.models import Customer
from booking.models import Booking,Room
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','username', 'password', 'email','address','profile_pic']
class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','manager', 'room_no', 'room_type', 'is_available','price','no_of_days_advance','start_date','room_image','room_description']
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','room_no', 'user_id', 'start_day', 'end_day','amount','booked_on']