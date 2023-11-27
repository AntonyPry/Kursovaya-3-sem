# rentals/admin.py

from django.contrib import admin
from .models import Car, Rental
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CarResource(resources.ModelResource):
    class Meta:
        model = Car

class CarAdmin(ImportExportModelAdmin):
    resource_class = CarResource
    list_display = ['brand', 'model', 'year', 'price_per_day', 'is_available']
    search_fields = ['brand', 'model']
    list_filter = ['year', 'is_available']  #фильтр по году и доступности

class RentalResource(resources.ModelResource):
    class Meta:
        model = Rental

class RentalAdmin(ImportExportModelAdmin):
    resource_class = RentalResource
    list_display = ['user', 'car', 'start_date', 'end_date', 'status']
    search_fields = ['user__username', 'car__brand', 'car__model']
    list_filter = ['status']  #фильтр по статусу аренды

admin.site.register(Car, CarAdmin)
admin.site.register(Rental, RentalAdmin)