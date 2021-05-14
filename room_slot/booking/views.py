from django.shortcuts import render,redirect
from .models import Contact
from .models import Room, Booking
from .forms import Search_By_Type
from login.models import Customer
from django.contrib import messages
from django.http import HttpResponse
import datetime
import folium

def index(request):
    qs = Room.objects.all()
    form = Search_By_Type()
    m = folium.Map(width=1200, height=600, location=[12.034516, 92.676842], zoom_start=12)
    
    folium.Marker(location = [12.034516, 92.676842],icon = folium.Icon(color='purple')).add_to(m)
    m = m._repr_html_()
    return render(request,'booking/index.html', {"Room": qs, "form": form, "map": m})


def contact(request):
    if request.method=="GET":
     return render(request,"contact/contact.html",{})
    else:
     username=request.POST['name']
     email=request.POST['email']
     message=request.POST['message']
     data=Contact(name=username,email=email,message=message)
     data.save()
     return render(request,"contact/contact.html",{'message':'Thank you for contacting us.'})
def book(request):
    if request.method=="POST":
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        #form = Search_By_Type(request.POST)
        room_type=request.POST['room_type']
        #print(request.POST)
        #print(form)
        #if form.is_valid():
        #    room_type = form.cleaned_data['room_type']
        #    print(form.cleaned_data)
        #else:
        #    print('pizdec')
        #    print(form.errors)
        request.session['start_date']=start_date
        request.session['end_date']=end_date
        start_date=datetime.datetime.strptime(start_date, "%d/%b/%Y").date()
        end_date=datetime.datetime.strptime(end_date, "%d/%b/%Y").date()
        no_of_days=(end_date-start_date).days
        #data=Room.objects.filter(is_available=True,no_of_days_advance__gte=no_of_days,start_date__lte=start_date)
        
        if room_type != 'All':
            data=Room.objects.filter(is_available=True,no_of_days_advance__gte=no_of_days,start_date__lte=start_date, room_type=room_type)
        else:
           data=Room.objects.filter(is_available=True,no_of_days_advance__gte=no_of_days,start_date__lte=start_date)
        request.session['no_of_days']=no_of_days
        return render(request,'booking/book.html',{'data':data})
    else:
        return redirect('index')
def book_now(request,id):
    if request.session.get("username",None) and request.session.get("type",None)=='customer':
        if request.session.get("no_of_days",1):
            no_of_days=request.session['no_of_days']
            start_date=request.session['start_date']
            end_date=request.session['end_date']
            request.session['room_no']=id
            data=Room.objects.get(room_no=id)
            bill=data.price*int(no_of_days)
            request.session['bill']=bill
            roomManager=data.manager.username
            return render(request,"booking/book-now.html",{"no_of_days":no_of_days,"room_no":id,"data":data,"bill":bill,"roomManager":roomManager,"start":start_date,"end":end_date})
        else:
            return redirect("index")
    else:
        next="book-now/"+id
        return redirect('user_login')
def book_confirm(request):
    room_no=request.session['room_no']
    start_date=request.session['start_date']
    end_date=request.session['end_date']
    username=request.session['username']
    user_id=Customer.objects.get(username=username)
    room=Room.objects.get(room_no=room_no)
    amount=request.session['bill']
    start_date=datetime.datetime.strptime(start_date, "%d/%b/%Y").date()
    end_date=datetime.datetime.strptime(end_date, "%d/%b/%Y").date()
    data=Booking(room_no=room,start_day=start_date,end_day=end_date,amount=amount,user_id=user_id)
    data.save()
    room.is_available=False
    room.save()
    del request.session['start_date']
    del request.session['end_date']
    del request.session['bill']
    del request.session['room_no']
    messages.info(request,"Room has been successfully booked")
    return redirect('user_dashboard')
def cancel_room(request,id):
    data=Booking.objects.get(id=id)
    room=data.room_no
    room.is_available=True
    room.save()
    data.delete()
    return HttpResponse("Booking Cancelled Successfully")
def delete_room(request,id):
    data=Room.objects.get(id=id)
    manager=data.manager.username
    if manager==request.session['username']:
        data.delete()
        return HttpResponse("You have deleted the room successfully")
    else:
        return HttpResponse("Invalid Request")


            



    
