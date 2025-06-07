from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from car.models import City
from django.contrib.auth.decorators import login_required
from .models import Car,YourOrders
import random
from datetime import date
import datetime
from django.contrib import messages

today = date.today()
print(today)
code=random.randint(100000,999999)
today = today.strftime('%Y-%m-%d')
print(today)

# Create your views here.

def rent(request):
    searchTerm = request.GET.get('s')
    if searchTerm:
        cars = Car.objects.filter(carname__icontains=searchTerm)
    else:
        cars = Car.objects.all()
    return render(request,'rent.html',{'search': searchTerm,'carrents': cars})


@login_required
def detail(request, car_id):
    cardetail = get_object_or_404(Car, pk=car_id)
    if request.user.is_authenticated:
        username = request.user.username
    
    hours = request.GET.get('hours')
    city = request.GET.get('city', '').strip()
    date = request.GET.get('date')
    name = request.GET.get('name')
    phone = str(request.GET.get('phonenumber'))
    
    cardata = get_object_or_404(Car, id=car_id)
    
    if len(phone) == 10:
        if hours:
            if City.objects.filter(city__iexact=city).exists():
                phonenumber = phone
                data = YourOrders(
                    user_name=username,
                    car=car_id,
                    hour=hours,
                    fullname=name,
                    phone=phonenumber,
                    travel_date=date,
                    fk=cardata,
                    code=code,
                    city=city
                )
                data.save()
                
                # Add success message
                messages.success(request, "Booking successful!")
                
                # Redirect to my orders
                return redirect('myorders')  # Adjust the URL name as needed
            else:
                messages.error(request, 'City not found')
        else:
            messages.error(request, 'Enter hours')
    else:
        messages.error(request, 'Enter valid phone number')
    
    return render(request, 'details.html', {
        'today': today,
        'cardetails': cardetail,
        'hours': hours,
        'city': city,
    })


       
@login_required
def myorders(request):
    if request.user.is_authenticated:
        username = request.user.username
    ordersdetails = YourOrders.objects.filter(user_name=username)
    return render(request, 'myorders.html', {
        'orders': ordersdetails,
        'today': date.today()
    })