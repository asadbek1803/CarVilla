from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Clients, New_cars, Feature_cars, Brands, Service
# Register your models here.

@admin.register(Clients)
class ClientsAdmin(ModelAdmin):
    list_display = ('id', 'client_full_name', 'message', 'country', 'client_image')
    list_filter = ('country', )
    list_editable = ('message', 'country')
    search_help_text = ("Klent qidiruv? ")
    search_fields = ('client_full_name', 'id', 'country')

@admin.register(New_cars)
class New_CarsAdmin(ModelAdmin):
    list_display = ('id', 'car_name', 'car_about', 'car_image')
    list_filter = ('id', 'car_name')
    list_editable = ('car_about', )
    search_help_text = ('Mashinalar qidiruv? ')
    search_fields = ('car_name', 'id')

@admin.register(Feature_cars)
class Feature_carsAdmin(ModelAdmin):
    list_display = ('id', 'car_name', 'about', 'price', 'car_type', 'horse_power', 'model', 'year')
    list_filter = ('id', 'price', 'car_type', 'year')
    list_editable = ('price', 'horse_power', 'model', 'year')
    search_help_text = ('Mashina qidiruv feature? ')
    search_fields = ('id', 'car_name', 'price', 'year')

@admin.register(Brands)
class BrandsAdmin(ModelAdmin):
    list_display = ('id', 'brand_name', 'image')
    list_filter = ('id', )

    search_help_text = (
        'Brand qidiruv? '
    )
    search_fields = ('id', 'brand_name')

@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ('id', 'title', 'about')
    list_filter = ('id', )
    list_editable = ('about', )
    search_help_text = ('Servis qidiruv? ')
    search_fields = ('id', 'title')
