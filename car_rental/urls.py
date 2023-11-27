# car_rental/urls.py

from django.contrib import admin
from django.urls import path, include
from rentals.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rentals.urls')),
    path('', index, name='index'),
]