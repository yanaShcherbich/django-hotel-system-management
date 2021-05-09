from django import forms
from .models import Room

class Search_By_Type(forms.Form):
    CHOICES = (('Single Room', 'Single Room'),('Double Room', 'Double Room'), ('Deluxe Room', 'Deluxe Room'), ('Super Deluxe Room', 'Super Deluxe Room'),)
    room_type = forms.ChoiceField(choices=CHOICES, label="Select room type:")