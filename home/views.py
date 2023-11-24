from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth import logout
from .models import Service, New_cars, Feature_cars, Clients, Brands
from rest_framework import viewsets, generics
from .serializers import CarSearchSerializer

from rest_framework import filters

# Create your views here.


@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    def get(self, request):
        data = {
            'services': Service.objects.all(),
            'new_cars': New_cars.objects.all(),
            'featured_cars': Feature_cars.objects.all(),
            'clients': Clients.objects.all(),
            'brands': Brands.objects.all()

        }
        return render(request, "index.html", data)

    def post(self, request):
        if request.POST:
            year = request.POST.get('year')
            horse_power = request.POST.get('hp')
            car_name = request.POST.get('car_name')
            model = request.POST.get('model')
            price = request.POST.get('price')

            return redirect(f"search/?search={year}&&?search={horse_power}&&?search={car_name}&&?search={model}&&?search={price}")




@method_decorator(login_required, name='dispatch')
class SearchViewSet(viewsets.ModelViewSet):
    queryset = Feature_cars.objects.all()
    serializer_class = CarSearchSerializer


@method_decorator(login_required, name='dispatch')
class SearchCarAPIVEW(generics.ListCreateAPIView):
    search_fields = ['year', 'horse_power', 'car_name', 'model', 'price']
    filter_backends = (filters.SearchFilter,)
    queryset = Feature_cars.objects.all()
    serializer_class = CarSearchSerializer

