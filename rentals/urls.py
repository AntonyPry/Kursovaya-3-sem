# rentals/urls.py

from django.urls import path
from .views import CarList, CarDetail, RentalList, RentalDetail, index, create_rental, user_rentals


urlpatterns = [
    path('', index, name='index'),
    path('cars/', CarList.as_view(), name='car_list'),
    path('cars/<int:pk>/', CarDetail.as_view(), name='car_detail'),
    path('rentals/', RentalList.as_view(), name='rental_list'),
    path('rentals/<int:pk>/', RentalDetail.as_view(), name='rental_detail'),
    path('create_rental/<int:car_id>/', create_rental, name='create_rental'),
    path('user_rentals/', user_rentals, name='user_rentals'),
]