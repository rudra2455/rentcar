"""rentcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from car import views as carView
from rent import views as rentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',carView.home,name='home'),
    path('rent/',rentView.rent,name='rent'),
    path('accounts/', include('account.urls')),
    path('rent/cardetails/', include('rent.urls')),
    path('city/',include('car.urls')),
    path('myorders/',rentView.myorders,name='myorders'),
    path('contact/',carView.contacts,name='contact'),
]

urlpatterns += static(settings.MEDIA_URL,
 document_root=settings.MEDIA_ROOT)