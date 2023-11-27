# rentals/views.py

from datetime import date, timedelta
from django.db.models import Q
from rest_framework import generics, viewsets, filters
from rest_framework.decorators import action, api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Car, Rental
from .serializers import CarSerializer, RentalSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RentalForm
from django.contrib.auth.decorators import login_required

@api_view(['GET'])
def index(request):
    return render(request, 'index.html')

class CarPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = CarPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['brand', 'model']

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    @action(detail=False, methods=['GET'])
    def ending_soon(self, request):
        queryset = Rental.objects.filter(
            Q(end_date__gte=date.today()) & Q(end_date__lte=date.today() + timedelta(days=7))
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def complete(self, request, pk=None):
        rental = self.get_object()
        rental.status = 'completed'
        rental.save()
        serializer = self.get_serializer(rental)
        return Response(serializer.data)

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'rentals/car_list.html'

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'cars': serializer.data})

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'rentals/car_detail.html'

class RentalList(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'rentals/rental_list.html'

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'rentals': serializer.data})

class RentalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'rentals/rental_detail.html'

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'rentals/car_list.html', {'cars': cars})

def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    return render(request, 'rentals/car_detail.html', {'car': car})

def rental_list(request):
    rentals = Rental.objects.all()
    return render(request, 'rentals/rental_list.html', {'rentals': rentals})

def rental_detail(request, pk):
    rental = Rental.objects.get(pk=pk)
    return render(request, 'rentals/rental_detail.html', {'rental': rental})

@login_required
def create_rental(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.user = request.user  # Установка текущего пользователя
            rental.car = car
            rental.save()
            return redirect('rental_list')
    else:
        form = RentalForm()

    return render(request, 'rentals/create_rental.html', {'form': form, 'car': car})

@login_required
def user_rentals(request):
    rentals = Rental.objects.filter(user=request.user)
    return render(request, 'rentals/user_rentals.html', {'rentals': rentals})