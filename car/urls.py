from django.urls import path
from car import views
urlpatterns = [
    path('cities/',views.cities,name='cities'),
    path('<int:order_id>/delete',views.deleteOrders,name='delete')
]