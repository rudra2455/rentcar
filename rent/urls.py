from django.urls import path
from rent import views
urlpatterns = [
    path('<int:car_id>', views.detail,name='detail'),
]