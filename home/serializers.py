from rest_framework import serializers
from .models import Feature_cars
class CarSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature_cars
        fields = ['year', 'horse_power', 'car_name', 'model', 'price']
