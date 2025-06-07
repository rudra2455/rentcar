from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from django.shortcuts import render,redirect
from .models import City,Contacts
from rent.models import Car
from rent.models import YourOrders

def home(request):
    topCars = Car.objects.order_by('price')[:3]
    return render(request,'home.html',{'cars':topCars})

def contacts(request):
    contacts_fullname = request.POST.get('fullname')
    contacts_email = request.POST.get('email')
    contacts_phone = request.POST.get('Phone')
    contacts_msg = request.POST.get('message')
    if (contacts_fullname and contacts_email and contacts_phone and contacts_msg):
        data = Contacts(fullname=contacts_fullname,email=contacts_email,phoneno=contacts_phone,message=contacts_msg)
        data.save()
        return redirect('/')
    else:
        return render(request,'contactus.html')

def cities(request):
    cities = City.objects.all()
    return render(request,'cities.html',{'cities':cities})

def deleteOrders(request,order_id):
    if request.user.is_authenticated:
        username = request.user.username
    orders = get_object_or_404(YourOrders, pk=order_id,user_name=username)
    orders.delete()
    return redirect('myorders')